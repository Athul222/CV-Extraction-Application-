# CV Extraction Application

## Objective

This is a Flask-based web application that allows the user to upload multiple files(`CV files`) of type pdf, doc, and docx. In which our program outputs a xls file which contains the following information such as the email, phone number and the remaining text of file.

## How To Use

A simple User Interface is provided to the user which has a upload and a download button in which you can upload multiple CV(of extension pdf, doc, docx) at the same time. You can download the extracted xls file by simply clicking on the download button provided on the UI

## Approach

1. **Installation and Setup**

- The srcipt requires the following modules to be installed to work effectively and efficiently.

    ### Libraries used
        1) PyPDF2:  Python library for PDF manipulation
        2) docx: Library to manipulate DOCX file
        3) subprocess: Library to manipulate DOC file
        4) re: tool for pattern matching
        5) openpyxl: Library for working with Excel files in Python.
        6) flask: Web framework for Python.
        7) werkzeug: Working with files uploaded by users through web forms
        8) os: for interacting with the file system
    
## Setup

1. **Install Python:**
    - Make sure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

2. **Clone the repository:**
    ```bash
    git clone ...
    ```

3. **Install Dependencis:**
    - Run the following command to install the required libraries:
    ```bash
    python -m pip install -r requirements.txt
    ```

## Run the Application

1. **Run the application**
    ```bash
    python app.py
    ```
    1. Access the application in your browser at http://localhost:5000.






