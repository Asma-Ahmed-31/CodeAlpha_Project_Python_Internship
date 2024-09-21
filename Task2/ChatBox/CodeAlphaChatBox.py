import nltk
from nltk.chat.util import Chat, reflections
import random

# Define patterns and responses
pairs = [
    [r'assalam alaikum|assalam o alaikum|assalam aliakum', ['Assalam Alaikum! How can I assist you today?', 'Assalam Alaikum! What can I help you with?']],
    [r'waliakum salam', ['How can I assist you?', 'How can I help you?']],
    [r'who are you|what is your name', ['I am a chatbot created to assist you with Python and general questions.']],
    [r'how are you', ["I'm just a program, but I'm doing great! How about you?"]],
    [r'i am good|i am good alhumdulilah|alhumdulilah', ['Alhumdulilah! How can I help you further?']],
    [r'who created you', ['I am created by Asma through programming.']],
    [r'bye|goodbye|allah hafiz', ['Allah Hafiz! Have a great day!', 'See you later!']],
    [r'what is the weather today?', ["I'm not connected to live weather services, but you can check online for accurate info!"]],
    [r'how old are you|age', ["I don't age, but I was created recently.", "Age is just a number, and mine is undefined!"]],
    [r'where are you|location', ["I'm a program, so I exist everywhere!", "I live in the cloud!"]],
    [r'favorite food|what do you eat|favourite food', ["I don't eat, but I hear pizza is a favorite!", 
                                        "I can't eat, but I imagine coding snacks are great!"]],
    [r'what are your hobbies|what do you like', ["I enjoy helping people with coding and questions.", 
                                                 "I don't have hobbies, but I like chatting with you!"]],
    [r'any informative idea', ["Do creative work to improve your skills."]],
    [r'how i feel better\?|i am sad what i do\?', ['Help others and doing great work may improve your mood.']],
    [r'.*', ["I'm sorry, I don't understand. Can you rephrase that?", 
             "Hmm, I didn't get that. Could you try again?"]]]

# Reflections to handle conversation mirroring
reflections = {
    'i am': 'you are',
    'i was': 'you were',
    'i': 'you',
    'i will': 'you will',
    'my': 'your',
    'you are': 'I am',
    'you were': 'I was'
}

# Create the Chatbot using nltk's Chat class
chatbot = Chat(pairs, reflections)

# Start the conversation
def chatbot_conversation():
    print("Chatbot: Assalam Alaikum! Type 'bye' or 'Allah Hafiz' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        if user_input in ['bye', 'goodbye', 'allah hafiz']:
            print(f"Chatbot: {random.choice(['Allah Hafiz! Have a great day!', 'See you later!'])}")
            break
        else:
            response = chatbot.respond(user_input)
            if response:
                print(f"Chatbot: {response}")
            else:
                print("Chatbot: Sorry, I don't understand that.")

# Run the chatbot
chatbot_conversation()

