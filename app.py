import streamlit as st
import requests
import io
from PIL import Image

st.set_page_config(page_title="Pro AI Image Bot", page_icon="🎨")
st.title("🎨 Pro AI Image Bot")

# Get your token from Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Using SDXL-Lightning: It's way more stable for free accounts
API_URL = "https://api-inference.huggingface.co/models/ByteDance/SDXL-Lightning"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    return None

prompt = st.text_input("What should the AI draw?", placeholder="A cool futuristic car...")

if st.button("Generate"):
    if prompt:
        with st.spinner("Drawing..."):
            image_bytes = query({"inputs": prompt})
            
            if image_bytes:
                try:
                    image = Image.open(io.BytesIO(image_bytes))
                    st.image(image, use_container_width=True)
                    st.success("There we go!")
                except:
                    st.error("The AI sent back something weird. Try again!")
            else:
                st.error("Model is still waking up. Wait 10 seconds and click Generate again!")
