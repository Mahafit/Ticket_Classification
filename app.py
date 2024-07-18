import streamlit as st
import re
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.neighbors import NearestNeighbors
from io import StringIO
import os
import asyncio
import aiohttp
from aiolimiter import AsyncLimiter
from langchain import HuggingFaceHub
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from tenacity import retry, stop_after_attempt, wait_random_exponential

# Load the balanced dataset
def load_data(chunk_size=30000):
    chunks = []
    for chunk in pd.read_csv('full_data_test.csv', chunksize=chunk_size):
        chunks.append(chunk)
    return pd.concat(chunks)

# Prepare the knowledge base
def prepare_knowledge_base(df):
    knowledge_base = df.apply(lambda row: f"Subject: {row['subject']}\nDescription: {row['description']}\nType: {row['ticket_type']}", axis=1).tolist()
    vectorizer = HashingVectorizer(n_features=2**18)
    knowledge_base_vectors = vectorizer.fit_transform(knowledge_base)
    nn = NearestNeighbors(n_neighbors=5, metric='cosine')
    nn.fit(knowledge_base_vectors)
    return knowledge_base, vectorizer, nn

def retrieve_relevant_info(query, vectorizer, nn, knowledge_base, top_k=5):
    query_vector = vectorizer.transform([query])
    distances, indices = nn.kneighbors(query_vector)
    return "\n\n".join([knowledge_base[i] for i in indices[0]])

def extract_email_subject(text):
    pattern = r"[:\]]\s*(.*)"
    match = re.search(pattern, text)
    if match:
        extracted_text = match.group(1).strip()
        if extracted_text:
            return extracted_text
    return text

def extract_email_body(text):
    def extract_plain_text_body(text):
        body_end_pattern = r"(?i)(\b(best regard(?:s)?|thanks|sincerely|see you soon|regards|ขอบคุณครับ|ขอบคุณค่ะ)\b)"
        match = re.search(body_end_pattern, text)
        if match:
            end_pos = match.start()
            return text[:end_pos].strip()
        else:
            return text.strip()

    def extract_email_format_body(text):
        start_index = -1
        for header in ["เรียน", "ถึง", "Subject:", "Sent:", "Cc:", "To:", "From:", "noc"]:
            start_index = text.find(header)
            if start_index != -1:
                break

        if start_index != -1:
            end_index = text.find("\n", start_index)
            if end_index != -1:
                text = text[end_index:].strip()
        
        delimiter_pattern = r"-{50,}"
        body = re.sub(delimiter_pattern, "", text)
        return extract_plain_text_body(body)

    email_headers_pattern = r"^(From|To|Subject|Date|Message-ID|เรียน|ถึง|เรื่อง):"
    if re.search(email_headers_pattern, text, re.MULTILINE):
        return extract_email_format_body(text)
    else:
        return extract_plain_text_body(text)

def character(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"http", "", text)
    text = re.sub(r"\S+@\S+", "", text)
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"\"[^\"]*\"", "", text)
    text = re.sub(r"\([^)]*\)", "", text)

    metadata_patterns = [
        r"from:", r"to:", r"cc:", r"sent:", r"subject:", r"best regards", r"tel\.", r"mobile", r"e-mail",
        r"เรียน", r"ถึง", r"แจ้ง","วันที่", "เวลา"
    ]
    for pattern in metadata_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    thai_months = r'(มกราคม|กุมภาพันธ์|มีนาคม|เมษายน|พฤษภาคม|มิถุนายน|กรกฎาคม|สิงหาคม|กันยายน|ตุลาคม|พฤศจิกายน|ธันวาคม)'
    thai_months_short = r'(ม.ค|ก.พ|มี.ค|เม.ย|พ.ค|มิ.ย|ก.ค|ส.ค|ก.ย|ต.ค|พ.ย|ธ.ค)'
    thai_days = r'(อาทิตย์|จันทร์|อังคาร|พุธ|พฤหัสบดี|ศุกร์|เสาร์)'
    eng_days = r'(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)'
    format_eng_short = r'\b([0-9]{1,2})\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s*([0-9]{4})\b'

    date_patterns = [thai_months, thai_months_short, thai_days, eng_days, format_eng_short]
    for pattern in date_patterns:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)

    text = re.sub(r"\n+", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.replace("@", "at")
    text = text.replace("!", "").replace(",", "")
    text = re.sub(r"[^A-Za-z0-9ก-๙(),!?\'\`\s]", " ", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"(^[\-_]+|[\-_]+$|(?<=\W)[\-_]+|[\-_]+(?=\W))", " ", text)
    text = text.lower().strip()

    return text

# Set up the LLM chain
def setup_llm_chain(model_repo, temperature, top_p, max_new_tokens, repetition_penalty):
    llm = HuggingFaceHub(repo_id=model_repo,
                         model_kwargs={"temperature": temperature,
                                       "top_p": top_p,
                                       "max_new_tokens": max_new_tokens,
                                       "repetition_penalty": repetition_penalty})

    template = """
    You are an expert email classifier. Use the following retrieved similar examples to help with classification:

    {retrieved_info}

    Now, classify the following new email:
    Email Subject: {subject}
    Email Description: {description}

    Present CLUES (i.e., keywords, phrases, contextual information, semantic meaning, semantic relationships, tones, references) that support the classification of the input email.
    Next, deduce the diagnostic REASONING process from premises (i.e., clues, input, similar examples) that support the email classification.
    Finally, based on clues, reasoning and the input, categorize the overall CLASSIFICATION of the email as Request or Incident. Return only one word answer with only the category name that the given email text belongs to with Request or Incident.
    """
    prompt = PromptTemplate(input_variables=["retrieved_info", "subject", "description"], template=template)
    chain = LLMChain(llm=llm, prompt=prompt)
    return chain

def process_llm_output(llm_output: str) -> tuple:
    clues_match = re.search(r'CLUES:(.*?)(?=(?:REASONING|REASONING PROCESS|DIAGNOSTIC REASONING|DIAGNOSTIC REASONING PROCESS):|$)', llm_output, re.DOTALL | re.IGNORECASE)
    reasoning_match = re.search(r'(?:REASONING|REASONING PROCESS|DIAGNOSTIC REASONING|DIAGNOSTIC REASONING PROCESS):(.*?)(?=CLASSIFICATION:|$)', llm_output, re.DOTALL | re.IGNORECASE)
    
    clue = clues_match.group(1).strip() if clues_match else ""
    reason = reasoning_match.group(1).strip() if reasoning_match else ""

    classification_match = re.search(r'CLASSIFICATION:\s*(\w+)\s*$', llm_output, re.IGNORECASE)
    if classification_match:
        raw_classification = classification_match.group(1).strip().lower()
        classification = 'Incident' if raw_classification == 'incident' else 'Request'
    else:
        last_line = llm_output.strip().split('\n')[-1].lower()
        classification = 'Incident' if 'incident' in last_line else 'Request'

    confidence = min((len(clue.split()) + len(reason.split())) / 100, 1.0)
    return classification, clue, reason, confidence

@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(10))
async def get_classification_with_summary(chain, subject, description, retrieved_info):
    if len(retrieved_info) + len(subject) + len(description) > 15000:
        # Implement summarization logic here if needed
        pass
    
    llm_output = await chain.arun(subject=subject, description=description, retrieved_info=retrieved_info)
    return process_llm_output(llm_output)

async def process_email(session, row, chain, vectorizer, nn, knowledge_base, semaphore, rate_limiter):
    async with semaphore:
        async with rate_limiter:
            subject = extract_email_subject(row['subject'])
            subject = character(subject) or subject or row['subject']
            
            description = extract_email_body(row['description'])
            description = character(description) or description or row['description']
            
            retrieved_info = retrieve_relevant_info(f"{subject} {description}", vectorizer, nn, knowledge_base)
            try:
                classification, clues, reasoning, confidence = await get_classification_with_summary(chain, subject, description, retrieved_info)
                correct = classification == row['ticket_type']
                
                return (row['subject'], row['description'], clues, reasoning, classification, row['ticket_type'], confidence, correct)
            except Exception as e:
                st.error(f"Error processing email: {str(e)}")
                return None

async def process_batch(df_upload, chain, vectorizer, nn, knowledge_base):
    results = []
    semaphore = asyncio.Semaphore(10)
    rate_limiter = AsyncLimiter(20, 1)
    async with aiohttp.ClientSession() as session:
        tasks = [process_email(session, row, chain, vectorizer, nn, knowledge_base, semaphore, rate_limiter) for _, row in df_upload.iterrows()]
        for result in asyncio.as_completed(tasks):
            try:
                result = await result
                if result:
                    results.append(result)
            except Exception as e:
                st.error(f"Error in batch processing: {str(e)}")
    return results

# Streamlit app
st.title('Email Classification with RAG')

# Sidebar
st.sidebar.title("Email Classification App with RAG")
st.sidebar.info('This app classifies emails as either "Request" or "Incident" using an advanced language model with Retrieval-Augmented Generation (RAG).')

st.sidebar.header("How to Use")
st.sidebar.markdown("""
1. **Single Email**: Enter the subject and description in the main panel and click 'Classify Email'.
2. **Batch Classification**: Upload a CSV file with 'subject', 'description', and 'ticket_type' columns, then click 'Classify Batch'.
""")

# Model settings in sidebar
st.sidebar.header("Model Settings")
model_options = [
    "mistralai/Mixtral-8x7B-Instruct-v0.1",
    "meta-llama/Meta-Llama-3-8B-Instruct",
]

model_repo = st.sidebar.selectbox("Select Model", model_options, index=0)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.8, 0.1)
max_new_tokens = st.sidebar.number_input("Max New Tokens", 1, 4096, 4096, 1)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.95, 0.05)
repetition_penalty = st.sidebar.slider("Repetition Penalty", 1.0, 2.0, 1.1, 0.1)

# Load data and prepare knowledge base
df = load_data()
knowledge_base, vectorizer, nn = prepare_knowledge_base(df)

# Set up LLM chain
chain = setup_llm_chain(model_repo, temperature, top_p, max_new_tokens, repetition_penalty)

# Single email classification
st.header("Single Email Classification")
subject = st.text_input("Enter the email subject:")
description = st.text_area("Enter the email description:", height=200)

if st.button('Classify Email'):
    if subject and description:
        with st.spinner('Classifying email...'):
            subject = character(extract_email_subject(subject))
            description = character(extract_email_body(description))
            retrieved_info = retrieve_relevant_info(f"{subject} {description}", vectorizer, nn, knowledge_base)
            classification, clues, reasoning, confidence = asyncio.run(get_classification_with_summary(chain, subject, description, retrieved_info))

        st.success(f"Classification: {classification} (Confidence: {confidence:.2f})")
        
        with st.expander("See details"):
            st.subheader("Processed Subject:")
            st.write(subject)
            st.subheader("Processed Description:")
            st.write(description)
            st.subheader("Retrieved Information:")
            st.write(retrieved_info)
            st.subheader("Clues:")
            st.write(clues)
            st.subheader("Reasoning:")
            st.write(reasoning)
    else:
        st.error("Please enter both subject and description.")

# Batch classification
st.header("Batch Classification")
uploaded_file = st.file_uploader("Choose a CSV file with multiple emails", type="csv")

if uploaded_file is not None:
    df_upload = pd.read_csv(uploaded_file)
    if 'subject' in df_upload.columns and 'description' in df_upload.columns and 'ticket_type' in df_upload.columns:
        if st.button('Classify Batch'):
            results = asyncio.run(process_batch(df_upload, chain, vectorizer, nn, knowledge_base))
            
            # Create a DataFrame for easy analysis
            results_df = pd.DataFrame(results, columns=['Subject', 'Description', 'Clue', 'Reason', 'Predicted', 'Actual', 'Confidence', 'Correct'])

            # Display summary table
            st.subheader("Summary of Predictions vs Actual")
            summary_df = results_df[['Subject', 'Predicted', 'Actual', 'Confidence', 'Correct']]
            st.dataframe(summary_df.style.applymap(lambda x: 'background-color: lightgreen' if x else 'background-color: lightsalmon', subset=['Correct']))

            # Detailed results
            st.subheader("Detailed Classification Results:")
            for _, row in results_df.iterrows():
                color = "lightgreen" if row['Correct'] else "lightsalmon"
                with st.expander(f"{row['Subject'][:50]}... - Predicted: {row['Predicted']} | Actual: {row['Actual']} (Confidence: {row['Confidence']:.2f})"):
                    st.markdown(f"<div style='background-color: {color}; padding: 10px;'>", unsafe_allow_html=True)
                    st.write(f"Subject: {row['Subject']}")
                    st.write(f"Predicted: {row['Predicted']}")
                    st.write(f"Actual: {row['Actual']}")
                    st.write(f"Confidence: {row['Confidence']:.2f}")
                    st.write("Clues:")
                    st.write(row['Clue'])
                    st.write("Reasoning:")
                    st.write(row['Reason'])
                    st.markdown("</div>", unsafe_allow_html=True)

            # Comparison metrics
            y_true = results_df['Actual']
            y_pred = results_df['Predicted']
            st.subheader("Classification Report:")
            st.text(classification_report(y_true, y_pred))

            # Confusion Matrix Visualization
            st.subheader("Confusion Matrix:")
            cm = confusion_matrix(y_true, y_pred)
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
            ax.set_xlabel('Predicted')
            ax.set_ylabel('Actual')
            ax.set_title('Confusion Matrix')
            st.pyplot(fig)

            # Classification Distribution
            st.subheader("Classification Distribution:")
            fig, ax = plt.subplots()
            results_df['Predicted'].value_counts().plot(kind='bar', ax=ax)
            ax.set_title('Predicted Classification Distribution')
            ax.set_xlabel('Class')
            ax.set_ylabel('Count')
            st.pyplot(fig)

            # Save results
            csv_buffer = StringIO()
            results_df.to_csv(csv_buffer, index=False)
            
            st.download_button(
                label="Download Results as CSV",
                data=csv_buffer.getvalue(),
                file_name="classification_results_with_rag.csv",
                mime="text/csv"
            )
    else:
        st.error("The CSV file must contain 'subject', 'description', and 'ticket_type' columns.")

# Add some final information
st.sidebar.markdown("---")
st.sidebar.header("About")
st.sidebar.info("""
This app uses a Retrieval-Augmented Generation (RAG) approach to classify emails.
It leverages a pre-trained language model and a knowledge base to provide accurate classifications.
""")

st.sidebar.header("Support")
st.sidebar.markdown("For questions or issues, contact: support@example.com")

st.sidebar.markdown("---")
st.sidebar.text("App Version: 2.0.0 (with RAG)")