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

The Ticket_Classification project is a Streamlit-based application designed to classify emails as either "Request" or "Incident" using a Retrieval-Augmented Generation (RAG) approach. Key features include single email classification, batch processing, and detailed result visualization. The project is suitable for IT support teams and customer service departments looking to automate and streamline their ticket classification process. The `app.py` file contains the main application logic, while `requirements.txt` ensures consistent environment setup, and `setup.sh` and the `Procfile` facilitate deployment in server environments, making the application easy to deploy and use.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Email Classification | • Uses a Retrieval-Augmented Generation (RAG) approach to classify emails.<br>• Classifies emails as either "Request" or "Incident".<br>• Supports single email classification and batch processing.<br>• Provides detailed result visualization. |
| RAG Approach | • - No specific information found about the RAG approach in the provided project context. |
| Streamlit App | • **Main Application File**: `app.py` is the primary file for the Streamlit-based email classification tool.<br>• Classification Approach**: Uses a Retrieval-Augmented Generation (RAG) approach to classify emails as "Request" or "Incident".<br>• Functionalities**: Includes single email classification, batch processing, and detailed result visualization. |
| Deployment Configuration | • The `Procfile` specifies the command to run the web application using Streamlit, which is essential for deployment on platforms like Heroku.<br>• The `setup.sh` script configures Streamlit to run in a headless mode with CORS disabled and sets the server port, typically used for deployment in a server environment. |
| Dependency Management | • **requirements.txt**: Lists the Python package dependencies and their versions required for the project to run correctly.<br>• Role**: Ensures consistent environment setup across different development and deployment environments. |
| Headless Mode | • Configures Streamlit to run in a headless mode.<br>• Disables CORS to allow cross-origin requests.<br>• Sets the server port for deployment. |
| Batch Processing | • - No specific information found regarding batch processing in the provided project context. |


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
  | `Procfile` | - **Purpose**: The `Procfile` specifies the command to run the web application using Streamlit, essential for deployment on platforms like Heroku. |
  | `app.py` | `app.py` is the main application file for a Streamlit-based email classification tool that uses a Retrieval-Augmented Generation (RAG) approach to classify emails as either "Request" or "Incident". It includes functionalities for single email classification, batch processing, and detailed result visualization. |
  | `requirements.txt` | - **Purpose**: Lists the Python package dependencies and their versions required for the project to run correctly. |
  | `setup.sh` | This `setup.sh` script configures Streamlit to run in a headless mode with CORS disabled and sets the server port, typically used for deployment in a server environment. |
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

4. **Run setup script** (if needed for deployment):
   ```sh
   bash setup.sh
   ```

## Usage
To run the application, use the following command:
```sh
streamlit run app.py
```

If you are deploying the application on a platform like Heroku, you can use the `Procfile` to specify the command to run the web application:
```sh
web: streamlit run app.py
```

For more details, refer to the project's README or documentation. Look for `app.py`, `main.py`, or `package.json` scripts if additional configuration is needed.
