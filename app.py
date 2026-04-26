import streamlit as st
import requests
import io
import time
from PIL import Image

st.set_page_config(page_title="Instant AI Art", page_icon="⚡")
st.title("⚡ Fast AI Image Bot")
st.write("Using FLUX.1 (The fastest free model in 2026)")

# Using your Hugging Face Token from Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Switch to the 'Schnell' (Fast) model - it's designed for speed
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_art(prompt_text):
    # We send the request and wait up to 120 seconds for a response
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt_text}, timeout=120)
    
    if response.status_code == 200:
        return response.content
    elif response.status_code == 503:
        # This means the model is loading. We tell the user to wait.
        return "LOADING"
    else:
        return None

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        status_placeholder = st.empty()
        status_placeholder.info("Sending request to AI...")
        
        result = generate_art(prompt)
        
        if result == "LOADING":
            status_placeholder.warning("AI is warming up! Give it 30 seconds and click Generate again.")
        elif result:
            image = Image.open(io.BytesIO(result))
            status_placeholder.empty()
            st.image(image, use_container_width=True)
            st.success("Success!")
        else:
            st.error("Model is currently too busy. Try again in a minute!")
