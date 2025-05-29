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

The Ticket_Classification project is a Streamlit web application designed to classify emails as either "Request" or "Incident" using a language model and Retrieval-Augmented Generation (RAG). Key features include data loading, text processing, and batch classification, with a user-friendly interface for both single and batch inputs. The project is suitable for IT support teams and customer service departments, providing an efficient way to automate and streamline ticket classification, thereby improving response times and operational efficiency. The setup is streamlined with files like `requirements.txt`, `Procfile`, and `setup.sh` to ensure a smooth deployment process.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Web Application | • The web application is implemented using Streamlit, providing a user interface for classifying emails.<br>• It supports both single and batch email classification, using a language model and RAG for processing. |
| Streamlit Integration | • The `app.py` file implements a Streamlit web application for classifying emails.<br>• The `Procfile` specifies the command to run the web application using Streamlit.<br>• The `setup.sh` script configures Streamlit to run in headless mode, disable CORS, and use a specified port. |
| Email Classification | • The project uses a language model and Retrieval-Augmented Generation (RAG) for classifying emails.<br>• The web application, implemented in `app.py`, provides a user interface for classifying emails as either "Request" or "Incident".<br>• Functions for data loading, text processing, and batch classification are included in the application. |
| RAG Implementation | • - No specific information found regarding RAG Implementation in the provided project context. |
| Headless Mode | • The `setup.sh` script configures Streamlit to run in headless mode.<br>• Headless mode is used to run the Streamlit application without a graphical user interface, typically for server environments or automated processes. |
| CORS Management | • - The `setup.sh` script disables CORS, which is necessary for allowing the web application to handle cross-origin requests.
- No specific information found regarding further details on CORS management within the project. |
| Dependency Management | • The `requirements.txt` file lists the Python packages and their versions required for the project, ensuring a consistent environment for development and deployment.<br>• The `setup.sh` script may include steps to install dependencies listed in `requirements.txt` and configure the environment. |


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
  | `Procfile` | The `Procfile` specifies the command to run the web application, in this case, using Streamlit to execute `app.py`. |
  | `app.py` | This file implements a Streamlit web application for classifying emails as either "Request" or "Incident" using a language model and Retrieval-Augmented Generation (RAG). It includes functions for data loading, text processing, and batch classification, and provides a user interface for single and batch email classification. |
  | `requirements.txt` | This `requirements.txt` file lists the Python packages and their versions required for the project, ensuring a consistent environment for development and deployment. |
  | `setup.sh` | This script sets up a Streamlit configuration file to run in headless mode, disable CORS, and use a specified port. |
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

4. **Set up Streamlit configuration**:
   ```sh
   ./setup.sh
   ```

## Usage
To run the web application, use the following command:
```sh
streamlit run app.py
```

Alternatively, if you prefer to use the `Procfile` to manage the application, you can use:
```sh
foreman start
```

For more details, refer to the project's README or documentation. If the primary run command is not evident, look for `app.py`, `main.py`, or `package.json` scripts.
