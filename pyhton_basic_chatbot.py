import re
import random
from datetime import date as day
import time 
import wheather


RULES = [
    (r"\b(hi|hello|hey)\b", ["Hello!", "Hey there!", "Hi! How can I help?"]),
    (r"\bhow are you\b", ["I'm doing great, thanks!", "All good! How about you?"]),
    (r"\b(your name|who are you)\b", ["I'm Amban, a chatbot built in Python."]),
    (r"\b(thanks|thank you)\b", ["You're welcome!", "Happy to help!"]),
    (r"\b(bye|goodbye)\b", ["Goodbye!", "Have a nice day!See you later!"]),
    (r"\b(what can you do|help)\b", ["I can chat with you and answer your questions.", "I can assist you with various topics."]),
    (r"\b(weather|temperature)\b", ["I can't provide real-time weather updates, but you can check a weather website or app."]),
    (r"\b(time|date)\b", [f"The current time is {time.strftime('%H:%M:%S')} and the date is {day.today()}"]),
]


def reply(text):
    text = text.strip().lower()
    for pattern, responses in RULES:
        if re.search(pattern, text):
            return random.choice(responses)
    return "Sorry, I don't understand that yet."


print("DIWI : Hi! How can I help you today?")

while True:
    user = input("You: ")
    if user.strip().lower() in ["exit", "quit", "bye"]:
        print("DIWI: Goodbye!")
        break
    answer = reply(user)
    print("DIWI:", answer)