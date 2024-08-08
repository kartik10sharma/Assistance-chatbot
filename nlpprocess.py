# nlpprocessing.py

import spacy

#  spaCy model is downloaded
try:
    nlp = spacy.load('en_core_web_sm')
except:
    import spacy.cli
    spacy.cli.download("en_core_web_sm") 
    nlp = spacy.load('en_core_web_sm')

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
