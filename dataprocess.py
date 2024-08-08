# datapreprocessor.py


from pdf2py import extract_text_from_pdfs, clean_text
from corelogic import main_bot_function
from tokenization import spacy_tokenize
from nlpprocess import process_with_nlp

def main():
    # PDF folder
    pdf_folder_path = r"C:\Users\karti\OneDrive\Documents\GitHub\chatbot\datapdf"
    
    # Extract text from PDFs
    raw_text = extract_text_from_pdfs(pdf_folder_path)
    print("Raw extracted text:", raw_text[:1000])  #  first 1000 characters

    # Clean the extracted text
    cleaned_text = clean_text(raw_text)
    print("Cleaned text:", cleaned_text[:1000])  #  first 1000 characters

    # Tokenize the cleaned text
    tokenized_texts = spacy_tokenize(cleaned_text)
    print("Tokenized text:", tokenized_texts[:50])  #  first 50 tokens
     
    # Process with NLP
    nlp_processed_data = process_with_nlp(tokenized_texts)
    print("NLP Processed Data:", nlp_processed_data[:1000])  #  first 1000 characters

    # Pass cleaned and tokenized data to chatbot logic
    main_bot_function(nlp_processed_data)

if __name__ == "__main__":
    main()
