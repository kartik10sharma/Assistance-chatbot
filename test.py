# app.py
from flask import Flask, render_template, request, jsonify
import fitz  # PyMuPDF
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.json.get('text')
    print(f"Received input: {user_input}")  
    nlp_processed_data = nlp_process(user_input)  
    response = main_bot_function(nlp_processed_data) 
    print(f"Result: {response}") 
    return jsonify({"response":response})

def nlp_process(input_text):
    
    return {
        "entities": ["Example Entity"],
        "pos_tags": ["NN", "VB"],
        "sentences": ["This is an example sentence."],
        "keywords": input_text.split()
    }

import PyPDF2

def search_pdf(keywords, pdf_path):
    excerpts = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            for keyword in keywords:
                if keyword.lower() in text.lower():
                    start_idx = text.lower().index(keyword.lower())
                    excerpt = text[max(0, start_idx - 50):start_idx + 80]  
                    excerpts.append(excerpt)
    return excerpts

def main_bot_function(nlp_processed_data):
   
    entities = nlp_processed_data["entities"]
    pos_tags = nlp_processed_data["pos_tags"]
    sentences = nlp_processed_data["sentences"]
    keywords = nlp_processed_data["keywords"]

   
    print("Named Entities:", entities)
    print("Part-of-Speech Tags:", pos_tags)
    print("Sentences:", sentences)
    print("Keywords:", keywords)

   
    intents = {
        "symptom_check": {
            "keywords": ["symptom", "feeling", "pain", "ache", "cough", "fever"],
            "response": "Please provide more details about your symptoms, such as duration, intensity, and any other related symptoms."
        },
        "find_doctor": {
            "keywords": ["doctor", "physician", "specialist", "appointment"],
            "response": "What kind of doctor are you looking for? (e.g., general physician, cardiologist, dermatologist)"
        },
        "medication_info": {
            "keywords": ["medication", "drug", "medicine", "prescription"],
            "response": "Please provide the name of the medication you want to know about."
        },
        "health_tips": {
            "keywords": ["health tips", "wellness", "nutrition", "exercise"],
            "response": "Here are some health tips: Eat a balanced diet, exercise regularly, get enough sleep, and stay hydrated."
        }
    }

    
    user_intent = None
    for intent, details in intents.items():
        if any(keyword.lower() in (kw.lower() for kw in keywords) for keyword in details["keywords"]):
            user_intent = intent
            break

    
    if user_intent:
        intent_response = intents[user_intent]["response"]
        response = {"intent_response": intent_response}
    else:
        intent_response = "I'm sorry, I couldn't understand your query. Here is some information from our database that might help:"
        
        pdf_path = r"C:\Users\karti\OneDrive\Documents\GitHub\chatbot\datapdf\Cloud Computing Terminology.pdf"  
        excerpts = search_pdf(keywords, pdf_path)

        response = {
            "intent_response": intent_response,
            "excerpts": excerpts
        }

    print("Response:", response)
    return response



if __name__ == '__main__':
    app.run(debug=True)



