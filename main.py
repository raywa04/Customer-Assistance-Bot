import PyPDF2
from transformers import pipeline
import os

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            for page_num in range(num_pages):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {str(e)}")
        return None

pdf_directory = '/Users/rayyanwaris/Desktop/EPSoft/SocialMedia/Input'

pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

pdf_texts = [extract_text_from_pdf(os.path.join(pdf_directory, pdf_file)) for pdf_file in pdf_files]

pdf_texts = [text for text in pdf_texts if text is not None]

def answer_questions(pdf_texts, question):
    combined_text = " ".join(pdf_texts)
    question_answering = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad", device=0)
    result = question_answering(question=question, context=combined_text)
    return result['answer']

pdf_directory = '/Users/rayyanwaris/Desktop/EPSoft/SocialMedia/Input'
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
pdf_texts = [extract_text_from_pdf(os.path.join(pdf_directory, pdf_file)) for pdf_file in pdf_files]

while True:
    user_question = input("Ask a question (type 'exit' to quit): ")
    if user_question.lower() == 'exit':
        break

    answer = answer_questions(pdf_texts, user_question)
    print(f"Answer: {answer}")
