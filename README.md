# <div align='center'>Ticket_Classification</div>

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

The Ticket_Classification repository is designed to classify emails using a Retrieval-Augmented Generation (RAG) approach, featuring a Streamlit web application and dependency management through a `requirements.txt` file. Key features include the ability to classify emails as "Request" or "Incident" using an advanced language model, and a streamlined setup process with `setup.sh` and `Procfile` for Heroku deployment. This tool is intended for customer support teams and other users who need to efficiently and accurately classify emails, enhancing productivity and workflow efficiency.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Email Classification | • The Ticket_Classification repository uses a Retrieval-Augmented Generation (RAG) approach for email classification.<br>• The tool is intended for users who need to classify emails, such as customer support teams.<br>• The system is designed to provide an efficient and accurate email classification, streamlining workflows and improving productivity.<br>• The Streamlit web application classifies emails as either "Request" or "Incident" using an advanced language model. |
| Streamlit App | • The `app.py` file serves as the main application file for the Streamlit web application.<br>• The Streamlit app classifies emails as either "Request" or "Incident" using an advanced language model with a Retrieval-Augmented Generation (RAG) approach.<br>• The app is designed to provide an efficient and accurate email classification system, streamlining workflows and improving productivity. |
| Dependency Management | • The `requirements.txt` file is used to specify the dependencies required to run the Python project.<br>• The file ensures that all necessary packages and their versions are installed, allowing the project to run correctly. |
| Web Deployment | • The `Procfile` specifies the command to run the Streamlit app in a Heroku environment.<br>• The `setup.sh` file configures the Streamlit server by creating a `config.toml` file with specific settings.<br>• The `app.py` file serves as the main application file for the Streamlit web application, which is deployed using Heroku. |
| Project Setup | • The `setup.sh` file is used to create a directory for Streamlit configuration and generate a `config.toml` file with specified server settings for Streamlit.<br>• The `Procfile` specifies the command to run the Streamlit app, which is essential for deploying the application on Heroku.<br>• The `requirements.txt` file lists the Python packages and their versions required for the project to run correctly. |
| RAG Approach | • The Ticket_Classification repository uses a Retrieval-Augmented Generation (RAG) approach for email classification.<br>• The RAG approach enhances the classification process by integrating retrieval mechanisms with generative models.<br>• The system is designed to provide an efficient and accurate email classification, streamlining workflows and improving productivity. |
| User Interface | • The Streamlit web application classifies emails as either "Request" or "Incident" using an advanced language model.<br>• The `app.py` file serves as the main application file for the Streamlit web application, utilizing a Retrieval-Augmented Generation (RAG) approach for email classification. |


## Project Structure

```text
Ticket_Classification_doc_gen_temp/
    ├── Procfile
    ├── README.md
    ├── app.py
    ├── requirements.txt
    └── setup.sh
```

### Project Index

This section provides detailed summaries for key files, grouped by directory.

<details open><summary><strong> Ticket_Classification/</strong> (Root Project Directory)</summary>

<details open><summary>  <strong> Files in _root_</strong> (5 files)</summary>

  | File Name | Summary (Primary Purpose) |
  |-----------|---------------------------|
  | `Procfile` | to specify the command that should be executed to start the web application in a Heroku environment |
  | `README.md` | to provide an overview and guide for the Ticket_Classification project, a Streamlit web application designed for email classification using a Retrieval-Augmented Generation (RAG) approach |
  | `app.py` | to provide a Streamlit web application for classifying emails as either "Request" or "Incident" using an advanced language model with Retrieval-Augmented Generation (RAG) |
  | `requirements.txt` | to specify the Python packages and their versions required for the project to run correctly |
  | `setup.sh` | to configure the Streamlit server by creating a configuration file with specific settings |

  **Detailed Summaries for this directory:**

  <details><summary><code>Procfile</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'Procfile' is to specify the command that should be executed to start the web application in a Heroku environment.

Key functionalities:
* Defines the process type (web) and the command to run the application.
* Ensures the application is accessible via a web server.

Role within the project architecture:
* Configures the entry point for the web application.
* Facilitates the deployment and scaling of the application on Heroku.

In summary, this 'Procfile' specifies the command to run the Streamlit application, ensuring it is correctly set up and accessible as a web service in the Heroku environment.
  ```
  </details>

  <details><summary><code>README.md</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'README.md' is to provide an overview and guide for the Ticket_Classification project, a Streamlit web application designed for email classification using a Retrieval-Augmented Generation (RAG) approach. This file serves as the central documentation for the project, covering its features, setup, and usage.

Key functionalities:
* Provides a table of contents for easy navigation
* Includes an overview of the project's purpose and features
* Outlines the project structure and key files
* Offers a step-by-step guide for getting started with the project

Role within the project architecture:
* Serves as the main documentation file for the project
* Provides instructions for setting up and running the application
* Offers an overview of the project's features and functionalities
* Not explicitly detailed from the provided content: Specific technical interactions with other components.

In summary, this 'README.md' plays a crucial role in onboarding users and developers to the Ticket_Classification project, providing essential information for understanding, setting up, and utilizing the email classification application.
  ```
  </details>

  <details><summary><code>app.py</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'app.py' is to provide a Streamlit web application for classifying emails as either "Request" or "Incident" using an advanced language model with Retrieval-Augmented Generation (RAG).

Key functionalities:
* Load and prepare a dataset of emails for classification.
* Extract and preprocess email subjects and descriptions.
* Retrieve relevant information from a knowledge base using a Nearest Neighbors model.
* Set up and use a language model (LLM) chain for classification.
* Classify single emails and batches of emails, providing detailed classification results and visualizations.

Role within the project architecture:
* Acts as the main entry point for the email classification application.
* Integrates data loading, preprocessing, and model inference components.
* Provides a user-friendly interface for both single and batch email classification.

In summary, this 'app.py' serves as the central component of the email classification system, combining data preparation, model inference, and user interaction to provide accurate and detailed email classifications.
  ```
  </details>

  <details><summary><code>requirements.txt</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'requirements.txt' is to specify the Python packages and their versions required for the project to run correctly.

Key functionalities:
* Lists the dependencies needed for the project, ensuring consistent environments across different machines.
* Specifies exact versions of the packages to avoid compatibility issues.

Role within the project architecture:
* Ensures that all necessary libraries are installed when setting up the project environment.
* Facilitates the setup process by providing a clear list of dependencies for tools like `pip`.

In summary, this 'requirements.txt' plays a crucial role in maintaining the project's environment by listing all required Python packages and their versions, ensuring that the project runs consistently across different setups.
  ```
  </details>

  <details><summary><code>setup.sh</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'setup.sh' is to configure the Streamlit server by creating a configuration file with specific settings.

Key functionalities:
* Creates the directory `~/.streamlit/` if it does not exist.
* Writes a configuration file `config.toml` with settings for the Streamlit server, including setting the server to headless mode, disabling CORS, and configuring the server port.

Role within the project architecture:
* Ensures that the Streamlit server is set up with the necessary configurations for headless operation and port settings.
* Facilitates the proper initialization of the Streamlit application environment.

In summary, this 'setup.sh' script plays a crucial role in setting up the Streamlit server environment by configuring essential parameters, ensuring that the application runs correctly in a headless mode and on the specified port.
  ```
  </details>

</details>


</details>


## Getting Started

### Prerequisites
- **Programming Language**: Python 3.x
- **Package Manager**: Pip
- **Other Requirements**: None explicitly mentioned.

### Installation
1. **Clone repository**:
   ```sh
   git clone https://github.com/Mahafit/Ticket_Classification.git
   ```

2. **Navigate to directory**:
   ```sh
   cd Ticket_Classification
   ```

3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure Streamlit**:
   Run the setup script to configure the Streamlit server:
   ```sh
   bash setup.sh
   ```

## Usage
1. **Run the Streamlit application**:
   ```sh
   streamlit run app.py
   ```

2. **Deploy to Heroku** (optional):
   If you want to deploy the application to Heroku, ensure you have a `Procfile` in your project directory. The `Procfile` should contain:
   ```sh
   web: streamlit run app.py
   ```

   Then, follow the Heroku deployment steps:
   ```sh
   heroku create
   git push heroku main
   heroku open
   ```

For more details, refer to the project's README or documentation. Look for `app.py` for the main application logic and `requirements.txt` for dependency management.
