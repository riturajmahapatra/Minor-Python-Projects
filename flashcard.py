import requests
import nltk
import re
import json
import os

nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

def load_flashcards(filename="flashcards.json"):
    """Load existing flashcards from a file."""
    if os.path.exists(filename):  # Check if file exists
        with open(filename, "r") as file:
            return json.load(file)
    return {}  # Return empty dictionary if no file


def save_flashcards(flashcards, filename="flashcards.json"):
    """Save flashcards to a file in JSON format."""
    with open(filename, "w") as file:
        json.dump(flashcards, file, indent=4)  # Pretty-print JSON


# 🟢 Load existing flashcards
flashcard_data = load_flashcards()

topic = input("Enter the topic for Flashcard: ").strip().replace(" ", "_")  # Format for URL
URL = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

response = requests.get(URL)  


if response.status_code == 200:
    data = response.json()  # Convert to JSON
    sentences = sent_tokenize(data['extract']) #extract sentences "Summary"
    flashcards = []
    if sentences:
        flashcards.append({"question": f"What is {topic}?", "answer": sentences[0]})

    # Create more flashcards (facts) from 1st index to rest
    for sentence in sentences[1:]:
        flashcards.append({"question": "What else?", "answer": sentence})

    flashcard_data[topic] = flashcards
    save_flashcards(flashcard_data)
    
    # Print flashcards
    for flashcard in flashcards:
        input(f"\nQ: {flashcard['question']} (Press Enter to see the answer...)")
        print(f"A: {flashcard['answer']}")
        input("\n(Press Enter for the next flashcard...)")


else:
    print("Bad Request")



