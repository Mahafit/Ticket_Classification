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

The Ticket_Classification project is designed to automate the classification of support tickets, enhancing efficiency and accuracy in customer service operations. Key features include a `requirements.txt` file that specifies the necessary Python dependencies, a `Procfile` that defines the command to run the application on Heroku, and a `setup.sh` script that configures the Streamlit server for deployment. This project is ideal for customer support teams and IT departments looking to streamline their ticket management processes, providing a valuable tool to improve response times and resource allocation.

## Features

| Feature          | Summary                                                      |
|------------------|--------------------------------------------------------------|
| Web Application | • The web application is launched using the command `streamlit run app.py` as specified in the `Procfile`.<br>• The `app.py` file is the entry point for the web application, likely containing the main logic and user interface for the ticket classification system. |
| Deployment Configuration | • Specifies the command to run the application using `streamlit run app.py` in the `Procfile`.<br>• Configures the Streamlit server settings via the `setup.sh` script, including creating the `~/.streamlit/` directory and writing the `config.toml` file. |
| Dependency Management | • Specifies dependencies for the project in `requirements.txt`.<br>• Ensures consistent environments across different development and deployment stages. |
| Streamlit Setup | • Creates a directory `~/.streamlit/` if it does not already exist.<br>• Writes a configuration file `config.toml` to the `~/.streamlit/` directory.<br>• Sets specific configurations in `config.toml` for the Streamlit server. |
| Process Definition | • Defines the process types and the command to run the application.<br>• Specifies that the `web` process should run the command `streamlit run app.py`. |


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
  | `Procfile` | - **Primary Purpose**: The `Procfile` is used to specify the commands that are executed by the Heroku platform to launch the application. |
  | `app.py` | ### Summary of `app.py` |
  | `requirements.txt` | - **Primary Purpose**: The `requirements.txt` file lists the Python packages and their specific versions required for the project to run correctly. |
  | `setup.sh` | - **Primary Purpose**: The `setup.sh` script is designed to configure the Streamlit server for a specific environment, likely a production or deployment environment. |
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

4. **Run setup script** (if necessary):
   ```sh
   bash setup.sh
   ```

## Usage
1. **Run the application**:
   ```sh
   python app.py
   ```

2. **Deploy on Heroku** (if using Heroku):
   - Ensure you have a `Procfile` in the root directory.
   - The `Procfile` specifies the command to run the application, typically:
     ```sh
     web: python app.py
     ```

For more details, refer to the project's README or documentation. Look for `app.py`, `main.py`, or `package.json` scripts if the primary run command is not evident.
