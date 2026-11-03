import os
from dotenv import load_dotenv
from google import genai

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables
api_key = os.getenv("API_KEY")

# Initialize the Gemini client
client = genai.Client(api_key=api_key)
# connect to Gemini
client = genai.Client(api_key=api_key)
#Create a chat session
chat = client.chats.create(model="gemini-3.8-flash")
print('Gemini chatbox Started (RTTCO & RAG Enabled!')    
print("Type 'exit'to stop.\n")
while True:
    message = input('you:')
    if message.lower() == "exit":
        print ('Goodbye!')
        break

    try:
        response = chat.send_message(message)
        print('Gemini:', response.text)     

    except Exception as error:
        print('Error', error)
