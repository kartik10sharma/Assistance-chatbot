# Assistant Chatbot
A Flask-based medical assistant chatbot designed to process natural language queries and provide relevant responses, including symptom checks, finding doctors, medication information, and health tips. The bot also has the capability to search for and display relevant excerpts from medical PDFs based on user queries.

## Key Features
- Natural Language Processing (NLP): The chatbot processes user inputs using basic NLP techniques to extract entities, keywords, and sentences.
- Symptom Check & Health Queries: The bot can respond to health-related queries by detecting user intent from keywords.
- PDF Integration: The bot can search a specified PDF document and extract relevant excerpts based on keywords detected in the user's query.
- Flask Web Interface: A simple, responsive web interface built with Flask and Tailwind CSS allows users to interact with the chatbot.
- Extensible Design: Easily add new intents and keywords to expand the bot's capabilities.
## Technologies & Libraries
- Flask: The core web framework used to handle routes and serve the chatbot interface.
- PyPDF2: A library used to extract text from PDF files, enabling the bot to search for and return relevant excerpts.
- JavaScript: Utilized in the frontend to handle user interactions and send messages to the server.
- Tailwind CSS: A utility-first CSS framework used to design a responsive and modern user interface.
- Natural Language Processing (NLP): Custom NLP functions process user inputs to extract meaningful data for intent recognition.
## Installation
Clone the Repository:

$ bash
Copy code
git clone https://github.com/kartik10sharma/Assistance-chatbot.git
cd Assistant-chatbot
Install Dependencies:
Ensure you have Python installed, then run:
$ bash
Copy code
pip install -r requirements.txt
Run the Application:

bash
Copy code
python app.py
The application will start on local system 

### Usage
Visit the web interface and type your health-related queries into the chatbot.
The bot will analyze your input, determine your intent, and respond accordingly.
For certain queries, the bot can extract and display relevant information from a specified PDF document.
Contributing
Feel free to fork this repository, make your improvements, and submit a pull request. Contributions are welcome!

## Some pics
![WhatsApp Image 2024-08-08 at 21 40 41](https://github.com/user-attachments/assets/2c9780a3-22d5-4afb-ba27-4a3531249a6e)
![WhatsApp Image 2024-08-08 at 21 51 05](https://github.com/user-attachments/assets/2d1601f5-e8ae-4120-a885-fa516656be1a)
![WhatsApp Image 2024-08-08 at 21 39 11](https://github.com/user-attachments/assets/862ecba4-8f42-4d84-8f10-53140d2b477c)
![WhatsApp Image 2024-08-08 at 21 45 31](https://github.com/user-attachments/assets/6d139f37-6196-4058-b283-cb40f0ad5890)
