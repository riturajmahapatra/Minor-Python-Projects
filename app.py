import streamlit as st
import requests
import nltk
from nltk.tokenize import sent_tokenize

# Download tokenizer (runs once)
nltk.download("punkt")

# Streamlit Page Config
st.set_page_config(page_title="AI Flashcards", page_icon="📖", layout="centered")

# Sidebar Header
st.sidebar.title("📌 Instructions")
st.sidebar.write("1️⃣ Enter a topic in the box.")  
st.sidebar.write("2️⃣ Click 'Generate Flashcards'.")  
st.sidebar.write("3️⃣ Click on a card to reveal the answer.")  

# App Title & Description
st.title("📚 AI-Powered Flashcards")
st.markdown("**Generate learning flashcards from Wikipedia summaries.**")

# User Input
topic = st.text_input("🔎 Enter a topic:").strip().replace(" ", "_")

if st.button("⚡ Generate Flashcards"):
    if topic:
        URL = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            sentences = sent_tokenize(data.get("extract", ""))  

            if sentences:
                st.success(f"✅ Flashcards for: **{topic.replace('_', ' ')}**")
                
                for i, sentence in enumerate(sentences[:5]):  
                    with st.expander(f"💡 Flashcard {i+1} (Click to Reveal)"):
                        st.write(sentence)
            else:
                st.warning("⚠️ No relevant data found. Try another topic.")
        else:
            st.error("❌ Failed to fetch data. Please try again.")
    else:
        st.warning("⚠️ Please enter a valid topic.")