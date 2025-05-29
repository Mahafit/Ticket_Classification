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

The Ticket_Classification project is a Streamlit-based application designed to classify emails as either "Request" or "Incident" using a Retrieval-Augmented Generation (RAG) approach. Key features include single email classification, batch processing, and detailed result visualization. The project is suitable for IT support teams and customer service departments looking to automate and streamline their ticket classification processes. By ensuring consistent environment setup and seamless deployment, the project's configuration files, such as `requirements.txt`, `Procfile`, and `setup.sh`, facilitate easy integration and maintenance, enhancing overall efficiency and accuracy in ticket management.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Email Classification | • Uses a Retrieval-Augmented Generation (RAG) approach to classify emails.<br>• Classifies emails into "Request" or "Incident" categories.<br>• Supports single email classification and batch processing.<br>• Provides detailed result visualization. |
| RAG Approach | • - No specific information found about the RAG approach in the provided project context. |
| Streamlit App | • The Streamlit app is the main application file (`app.py`) for a tool that classifies emails using a Retrieval-Augmented Generation (RAG) approach.<br>• It supports single email classification, batch processing, and detailed result visualization. |
| Deployment Configuration | • The `Procfile` specifies the command to run the web application using Streamlit, indicating how the application should be started in the deployment environment.<br>• The `setup.sh` script sets up the Streamlit server configuration, ensuring it runs headlessly, disables CORS, and uses a specified port.<br>• The `setup.sh` script creates and configures the `~/.streamlit/config.toml` file with the necessary settings. |
| Batch Processing | • - No specific information found regarding batch processing in the provided project context. |
| Result Visualization | • - No specific information found regarding result visualization in the provided project context. |
| Environment Setup | • **requirements.txt**: Lists the Python package dependencies and their versions required for the project to run correctly, ensuring consistent environment setup.<br>• setup.sh**: Sets up the Streamlit server configuration, including running headlessly, disabling CORS, and using a specified port, by creating and configuring the `~/.streamlit/config.toml` file. |


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
  | `Procfile` | - The `Procfile` specifies the command to run the web application using Streamlit, indicating how the application should be started in the deployment environment. |
  | `app.py` | `app.py` is the main application file for a Streamlit-based email classification tool that uses a Retrieval-Augmented Generation (RAG) approach to classify emails as either "Request" or "Incident". It includes functionalities for single email classification, batch processing, and detailed result visualization. |
  | `requirements.txt` | - **Purpose**: Lists the Python package dependencies and their versions required for the project to run correctly. |
  | `setup.sh` | - Sets up the Streamlit server configuration, ensuring it runs headlessly, disables CORS, and uses a specified port. |
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
To run the application, use the following command:
```sh
streamlit run app.py
```

Alternatively, if you are using a deployment environment that supports the `Procfile`, the application can be started using:
```sh
foreman start
```

For more details, refer to the project's README or documentation. If the primary run command is not evident, look for `app.py`, `main.py`, or `package.json` scripts.
