# Customer Assistance Chatbot with PDF Text Extraction

## Overview

This Python script is designed to create a customer assistance chatbot that extracts text from PDF files and answers user questions based on the combined content of multiple PDFs. The script utilizes the PyPDF2 library for PDF text extraction and the transformers library for question-answering using a pre-trained BERT model.

## Requirements

- Python 3.x
- PyPDF2 library
- Transformers library (Hugging Face)
- Pre-trained BERT model for question-answering

## Installation

1. Install Python: [Download and install Python](https://www.python.org/downloads/)

2. Install required libraries:

   ```bash
   pip install PyPDF2 transformers
   ```

3. Run the script:

   ```bash
   python your_script_name.py
   ```

## Usage

1. Place your PDF files in the specified directory.

2. Run the script.

3. Enter a question when prompted. The chatbot will provide an answer based on the content of the PDF files.

4. Type 'exit' to quit the chatbot.

## Configuration

- Update the `pdf_directory` variable with the path to the directory containing your PDF files.
- Modify the model in the `answer_questions` function as needed.

## Important Note

- Ensure that you have a stable internet connection for the first run, as the script might download the BERT model from the Hugging Face model hub.

## Disclaimer

This script is a simple example and may require further customization based on specific use cases and requirements.

Feel free to adapt and extend the code according to your needs!

```

Remember to replace `your_script_name.py` with the actual name of your Python script. Additionally, you may want to provide more details about the PDF file format expected and any other specifics related to the usage of your script.
