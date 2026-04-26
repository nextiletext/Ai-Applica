import streamlit as st
import requests
import io
import time
from PIL import Image

st.set_page_config(page_title="AI Art Generator", page_icon="🎨")
st.title("🎨 AI Art Generator")

HF_TOKEN = st.secrets["HF_TOKEN"]
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    # This loop will retry if the model is still loading
    for _ in range(3): 
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.content
        
        # Check if the model is still loading
        if response.status_code == 200:
            return output
        elif "estimated_time" in response.text:
            wait_time = response.json().get("estimated_time", 10)
            st.info(f"AI is waking up... waiting {int(wait_time)} seconds.")
            time.sleep(wait_time)
        else:
            continue
    return None

prompt = st.text_input("Describe your image:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Creating..."):
            image_bytes = query({"inputs": prompt})
            if image_bytes:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image)
                st.success("Done!")
            else:
                st.error("Model took too long to wake up. Try one more time!")
