# <div align='center'>Ticket_Classification</div>

<div align="center">
  <h1>Table of Contents</h1>
</div>

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

The Ticket_Classification repository is designed for email classification using a Retrieval-Augmented Generation (RAG) approach. Its key features include a Streamlit web application and dependency management through requirements.txt. The tool is intended for customer support teams and other users who need to classify emails. The repository provides an efficient and accurate email classification system, streamlining workflows and improving productivity.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Email Classification | • Based on the provided information, here are 2-4 key aspects of Email Classification:<br>• The Ticket_Classification repository uses a Retrieval-Augmented Generation (RAG) approach for email classification.<br>• The tool is intended for users who need to classify emails, such as customer support teams.<br>• The system is designed to provide an efficient and accurate email classification, streamlining workflows and improving productivity.<br>• The Streamlit web application classifies emails as either "Request" or "Incident" using an advanced language model. |
| Streamlit Configuration | • Based on the provided information, here are 2-4 key aspects of Streamlit Configuration:<br>• The `setup.sh` file is used to create a directory for Streamlit configuration.<br>• The `setup.sh` file generates a `config.toml` file with specified server settings for Streamlit.<br>• The `Procfile` declares process types and corresponding commands for a Heroku application, including the command to run the Streamlit app.<br>• The `app.py` file serves as the main application file for the Streamlit web application, utilizing a Retrieval-Augmented Generation (RAG) approach for email classification. |
| Dependency Management | • Based on the provided information, here are 2-4 key aspects of Dependency Management:<br>• The `requirements.txt` file is used to specify the dependencies required to run the Python project.<br>• The file lists the libraries and frameworks needed to run the project, along with their exact versions to ensure consistency and reproducibility.<br>• The `requirements.txt` file is used by package managers like pip to install the required dependencies.<br>• The project uses a specific version of each dependency, as specified in the `requirements.txt` file, to ensure reproducibility. |
| Web Application | • Based on the provided information, here are 2-4 key aspects of the Web Application:<br>• The web application is built using Streamlit, a Python library for building web applications.<br>• The application has a user interface.<br>• The application is used for email classification, utilizing a Retrieval-Augmented Generation (RAG) approach.<br>• The main application file for the Streamlit web application is `app.py`. |
| Process Declaration | • Based on the provided information, here are 2-4 key aspects of 'Process Declaration' as bullet points:<br>• The project utilizes a `Procfile` to declare process types and corresponding commands for a Heroku application.<br>• The `Procfile` specifies the command to run the Streamlit app.<br>• The file defines the command that should be executed when the application is launched, specifically for a web process.<br>• The `Procfile` is used to configure the application's runtime environment, ensuring the correct execution of the Streamlit application. |
| Project Setup | • Here are 2-4 key aspects of the 'Project Setup' as bullet points:<br>• The project uses a `requirements.txt` file to specify dependencies required to run the project.<br>• A `setup.sh` file is used to create a directory and configure Streamlit, including generating a `config.toml` file with specific server settings.<br>• The project utilizes a `Procfile` to declare process types and corresponding commands for a Heroku application, specifying the command to run the Streamlit app.<br>• The `app.py` file serves as the main application file for the Streamlit web application. |
| Retrieval Approach | • Based on the provided information, here are 2-4 key aspects of the 'Retrieval Approach' as bullet points:<br>• The project uses a Retrieval-Augmented Generation (RAG) approach for email classification.<br>• The RAG approach is utilized in the Streamlit web application to classify emails.<br>• The application uses an advanced language model with Retrieval-Augmented Generation to classify emails as either "Request" or "Incident".<br>• No additional specific details are provided about the Retrieval Approach beyond its application in email classification. |


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

<details open><summary><strong>▼ Ticket_Classification/</strong> (Root Project Directory)</summary>

<details open><summary>  <strong>▼ Files in _root_</strong> (5 files)</summary>

  | File Name | Summary (Primary Purpose) |
  |-----------|---------------------------|
  | `Procfile` | to define the command that should be executed when the application is launched, specifically for a web process |
  | `README.md` | to provide an overview and guide for the Ticket_Classification project, a Streamlit web application designed for email classification using a Retrieval-Augmented Generation (RAG) approach |
  | `app.py` | to create a Streamlit application for classifying emails as either "Request" or "Incident" using an advanced language model with Retrieval-Augmented Generation (RAG) |
  | `requirements.txt` | See details below. |
  | `setup.sh` | See details below. |

  **Detailed Summaries for this directory:**

  <details><summary><code>Procfile</code> - Full Details</summary>

  ```markdown
  The primary purpose of the 'Procfile' is to define the command that should be executed when the application is launched, specifically for a web process. It specifies that the `streamlit run app.py` command should be run to start the web application.

Key functionalities:
* Defines the command for the web process
* Specifies the execution of the `app.py` file using `streamlit run`
* Configures the application launch process

Role within the project architecture:
* Defines the web process launch configuration
* Interacts with the `app.py` file to start the application
* Not explicitly detailed from the provided content, as the specific project architecture and other interactions are not clear

In summary, this 'Procfile' plays a crucial role in configuring the launch of the web application by specifying the command to execute the `app.py` file, and its main contribution is to define the web process launch configuration for the project.
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
  The primary purpose of the 'app.py' is to create a Streamlit application for classifying emails as either "Request" or "Incident" using an advanced language model with Retrieval-Augmented Generation (RAG). This application allows users to classify single emails or batches of emails uploaded through a CSV file.

Key functionalities:
* Classify single emails based on their subject and description
* Classify batches of emails from a CSV file containing'subject', 'description', and 'ticket_type' columns
* Provide detailed classification results, including clues and reasoning for each email
* Display a summary of predictions vs actual classifications and offer a downloadable CSV file of the results

Role within the project architecture:
* Acts as the main application entry point, handling user input and interactions
* Utilizes a pre-trained language model and a knowledge base to generate accurate classifications
* Integrates with Streamlit to provide a user-friendly interface for email classification tasks

In summary, this 'app.py' serves as a central component of an email classification system, leveraging RAG and a user-friendly interface to provide accurate and informative email classifications, making it a valuable tool for email management and analysis tasks.
  ```
  </details>

  <details><summary><code>requirements.txt</code> - Full Details</summary>

  ```markdown
  The primary purpose of the'requirements.txt' is to list the dependencies required by a Python project, specifying the exact versions of libraries and frameworks needed to run the project. This file serves as a configuration file for package managers like pip to install the necessary dependencies.

Key functionalities:
* Specifies the version of each dependency to ensure compatibility and reproducibility
* Provides a list of libraries and frameworks used in the project, including data science tools like pandas and scikit-learn
* Enables easy installation of dependencies using package managers
* Helps in managing project dependencies across different environments

Role within the project architecture:
* Defines the project's dependencies and their versions
* Interacts with package managers like pip to install dependencies
* Plays a crucial role in ensuring the project's portability and reproducibility across different environments

In summary, this'requirements.txt' file is essential for configuring and managing the dependencies of a Python project, ensuring that all necessary libraries and frameworks are installed with the correct versions, which is critical for the project's stability and reproducibility.
  ```
  </details>

  <details><summary><code>setup.sh</code> - Full Details</summary>

  ```markdown
  The primary purpose of the'setup.sh' is to create a directory for Streamlit configuration and generate a configuration file with specified server settings. This script initializes the environment for a Streamlit application.

Key functionalities:
* Creates a directory at ~/.streamlit/ if it does not exist
* Generates a configuration file named config.toml with server settings
* Sets server properties such as headless mode, CORS enablement, and port number

Role within the project architecture:
* Configures the Streamlit server for headless operation
* Specifies the port for the Streamlit application to use
* Disables CORS (Cross-Origin Resource Sharing) for the server

In summary, this'setup.sh' script plays a crucial role in configuring the Streamlit server environment by creating the necessary directory structure and setting up the server configuration, which is essential for running a Streamlit application.
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
   Additionally, you may need to run the `setup.sh` script to configure Streamlit and generate the `config.toml` file:
   ```sh
  ./setup.sh
   ```

## Usage
   The primary run command is not explicitly stated, but based on the project structure, you can try running the Streamlit application using:
   ```sh
   streamlit run app.py
   ```
   Alternatively, if you have configured the project for deployment on Heroku, you can use the command specified in the `Procfile`. For more details, refer to the project's README or documentation.
