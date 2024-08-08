from flask import Flask, render_template, request, jsonify
import spacy
from test import search_pdf

try:
    nlp = spacy.load('en_core_web_sm')
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load('en_core_web_sm')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.json.get('text')
    print(f"Received input: {user_input}")  # Log input 
    nlp_processed_data = process_with_nlp(user_input)  # NLP processing
    response = main_bot_function(nlp_processed_data)  # Call main bot function
    print(f"Result: {response}")  # Log result 
    return jsonify({"response": response})

def process_with_nlp(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    pos_tags = [(token.text, token.pos_) for token in doc]
    keywords = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return {
        "entities": entities,
        "pos_tags": pos_tags,
        "keywords": keywords,
        "sentences": [sent.text for sent in doc.sents],
    }

def main_bot_function(nlp_processed_data):
    # Extracted NLP data
    entities = nlp_processed_data["entities"]
    pos_tags = nlp_processed_data["pos_tags"]
    sentences = nlp_processed_data["sentences"]
    keywords = nlp_processed_data["keywords"]

    # Print processed info for debugging
    print("Named Entities:", entities)
    print("Part-of-Speech Tags:", pos_tags)
    print("Sentences:", sentences)
    print("Keywords:", keywords)

    # Intents and responses
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

    # Determine user intent based on keywords
    user_intent = None
    for intent, details in intents.items():
        if any(keyword.lower() in (kw.lower() for kw in keywords) for keyword in details["keywords"]):
            user_intent = intent
            break

    #  response based on detected intent
    if user_intent:
        intent_response = intents[user_intent]["response"]
        response = {"intent_response": intent_response}
    else:
        intent_response = "I'm sorry, I couldn't understand your query. Here is some information from our database that might help:"
        # PDFs for keywords
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
