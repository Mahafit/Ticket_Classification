# <div align='center'> Ticket_Classification</div>


## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
  - [Project Index](#project-index)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)

---

## Overview

The Ticket_Classification repository is designed for email classification using a Retrieval-Augmented Generation (RAG) approach. Key features include a Streamlit web application and dependency management through requirements.txt. The tool is intended for users who need to classify emails, such as customer support teams. The value of this repository lies in its ability to provide an efficient and accurate email classification system, streamlining workflows and improving productivity.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Project Setup | • Here are 2-4 key aspects of the project setup:<br>• The project uses a `requirements.txt` file to specify dependencies required to run the project.<br>• A `setup.sh` file is used to create a directory and configure Streamlit, including generating a `config.toml` file with specific server settings.<br>• The project utilizes a `Procfile` to declare process types and corresponding commands for a Heroku application, specifying the command to run the Streamlit app.<br>• The `app.py` file serves as the main application file for the Streamlit web application. |
| Dependency Management | • Based on the provided information, here are 2-4 key aspects of Dependency Management:<br>• The `requirements.txt` file is used to specify the dependencies required to run the Python project.<br>• The file lists the libraries and frameworks needed to run the project, along with their exact versions to ensure consistency and reproducibility.<br>• The `requirements.txt` file is used by package managers like pip to install the required dependencies.<br>• The project uses a specific version of each dependency, as specified in the `requirements.txt` file, to ensure reproducibility. |
| Web Application | • Based on the project information, here are 2-4 key aspects of the Web Application:<br>• The web application is built using Streamlit, a Python library for building web applications.<br>• The application has a user interface where users can input email subjects and descriptions for classification.<br>• The application is designed to be deployed on Heroku, with a Procfile declaring the process types and corresponding commands.<br>• The application utilizes a Retrieval-Augmented Generation (RAG) approach for email classification. |
| Streamlit Configuration | • Here are 2-4 key aspects of Streamlit Configuration:<br>• The `setup.sh` file creates a directory at `~/.streamlit/` if it does not exist.<br>• A `config.toml` file is generated in the `~/.streamlit/` directory with specific Streamlit server settings.<br>• The Streamlit server is configured to run in headless mode.<br>• CORS is disabled in the Streamlit server settings. |
| Email Classification | • Here are 2-4 key aspects of Email Classification based on the project information:<br>• The project utilizes a Retrieval-Augmented Generation (RAG) approach for email classification.<br>• A Streamlit web application is used to create a user interface for email classification.<br>• Users can input email subjects and descriptions for classification through the application.<br>• The application uses a pre-trained language model for classification purposes. |
| Process Declaration | • Based on the provided information, here are 2-4 key aspects related to 'Process Declaration' as bullet points:<br>• The Procfile declares the process types and their corresponding commands for a Heroku application.<br>• It specifies the command to run the application, in this case, a Streamlit app.<br>• The process type is defined as 'web', indicating it's a web application.<br>• The Procfile is used by Heroku to determine how to run the application. |
| Application Entry | • Based on the provided information, here are 2-4 key aspects of the 'Application Entry' as bullet points:<br>• The main application file is `app.py`, which is the entry point for a Streamlit web application.<br>• The `app.py` file creates a user interface for email classification using a Retrieval-Augmented Generation (RAG) approach.<br>• The application utilizes a pre-trained language model for classification purposes.<br>• The application is set up to be run with specific commands and process types defined in the `Procfile`, which is used by Heroku to determine how to run the application. |


## Project Structure

```text
Ticket_Classification_doc_gen_temp/
    ├── Procfile
    ├── app.py
    ├── requirements.txt
    └── setup.sh
```

### Project Index

This section provides summaries for key files, grouped by directory. Note that summaries are AI-generated and may be concise.

<details open><summary><strong> Ticket_Classification/</strong> (Root Project Directory)</summary>

<details open><summary>  <strong> Files in _root_</strong> (4 files)</summary>

  | File Name | Summary |
  |-----------|---------|
  | `Procfile` | The primary purpose of the 'Procfile' is to declare the process types and their corresponding commands for a Heroku application. 

Key functionalities:
* It specifies the command to run the application, in this case, a Streamlit app.
* It defines the process type as 'web', indicating it's a web application.

Role within the project architecture:
* The 'Procfile' is used by Heroku to determine how to run the application.
* It's typically located in the root directory of the project.

In summary, this 'Procfile' configures Heroku to run a Streamlit web application using the command `streamlit run app.py`. |
  | `app.py` | **File Purpose and Primary Functionality:**
The provided file, `app.py`, is the main application file for a Streamlit web application designed for email classification using a Retrieval-Augmented Generation (RAG) approach. The primary functionality of this file is to create a user interface where users can input email subjects and descriptions for classification. It utilizes a pre-trained language model and a knowledge base to classify emails into two categories: "Request" or "Incident".

**Key Functionalities:**

* **Email Classification:** The application classifies input emails based on their subjects and descriptions.
* **Knowledge Base Preparation:** It prepares a knowledge base from a provided dataset to aid in the classification process.
* **Model Settings:** Users can adjust model settings such as temperature, max new tokens, top P, and repetition penalty to fine-tune the classification model.
* **Batch Classification:** The application supports batch classification, allowing users to upload a CSV file containing multiple emails for classification.
* **Results Analysis:** It provides a detailed analysis of the classification results, including a summary table, detailed classification results, and comparison metrics such as a classification report and a confusion matrix.

**Role within the Project Architecture:**
This file serves as the central component of the project, integrating all necessary functionalities for email classification, including data loading, model setup, and user interface creation. It is designed to be executed directly, launching the Streamlit application and making the email classification tool accessible to users.

**Configuration:**
The file configures the following:
- Model settings for the RAG approach
- The knowledge base used for classification
- The user interface for single and batch email classification
- The analysis and visualization of classification results

Overall, `app.py` is a comprehensive application file that encapsulates the core functionality of an email classification system using a RAG approach, providing both a user-friendly interface and in-depth analysis of classification results. |
  | `requirements.txt` | The primary purpose of the'requirements.txt' file is to specify the dependencies required to run a Python project. 

Key functionalities and roles:
* Lists the libraries and frameworks needed to run the project
* Specifies the exact version of each dependency to ensure consistency and reproducibility
* Used by package managers like pip to install the required dependencies

In the project architecture, this file serves as a configuration file for dependency management, allowing developers to easily install and manage the project's dependencies. 

The listed dependencies include:
* Data science libraries: pandas, numpy, scikit-learn, seaborn, matplotlib
* Web development libraries: streamlit, aiohttp, aiolimiter
* AI and machine learning libraries: langchain
* Utility libraries: tenacity 

Overall, the'requirements.txt' file plays a crucial role in ensuring the project's dependencies are properly managed and installed, making it easier to develop, test, and deploy the project. |
  | `setup.sh` | The primary purpose of the `setup.sh` file is to create a directory and configure Streamlit, a Python library for building web applications. 

Key functionalities:
* Create a directory at `~/.streamlit/` if it does not exist
* Generate a `config.toml` file in the `~/.streamlit/` directory with specific Streamlit server settings, including:
  * Running the server in headless mode
  * Disabling CORS (Cross-Origin Resource Sharing)
  * Setting the server port to an environment variable `$PORT`

Role within the project architecture: This script is likely used to initialize and configure a Streamlit application, possibly in a containerized or cloud environment where the port is dynamically assigned. The script ensures that the necessary directory and configuration file are in place for the Streamlit server to run with the specified settings. |
</details>


</details>


## Getting Started
The Ticket Classification project is a Streamlit web application designed for email classification using a Retrieval-Augmented Generation (RAG) approach. This guide provides a step-by-step process to get started with the project.

### Prerequisites
- **Programming Language**: Python 3.x
- **Package Manager**: Pip
- **Other Requirements**: None explicitly mentioned.

### Installation
1. **Clone repository**:
   ```sh
   git clone https://github.com/Mahafit/Ticket_Classification
   ```
2. **Navigate to directory**:
   ```sh
   cd Ticket_Classification
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
   Additionally, you can run the `setup.sh` script to configure Streamlit:
   ```sh
  ./setup.sh
   ```

## Usage
   To run the application, use the following command:
   ```sh
   python app.py
   ```
   Alternatively, you can refer to the `Procfile` for Heroku deployment instructions. If you're unsure about the primary run command, refer to the project's documentation or look for scripts in `app.py` or `package.json`. 

For more details, refer to the project's README or documentation.
