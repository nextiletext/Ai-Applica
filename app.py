import streamlit as st
import requests
import io
from PIL import Image

# 1. Page Config
st.set_page_config(page_title="Hugging Face Image Bot", page_icon="🤗")
st.title("🤗 Hugging Face Image Bot")
st.write("Generating art using open-source models (Free Tier).")

# 2. Secret Key Setup
# We pull this from your Streamlit Dashboard later
HF_TOKEN = st.secrets["HF_TOKEN"]

# The "Model" we are using (Stable Diffusion XL is great and reliable)
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# 3. The UI
prompt = st.text_input("What should the AI draw?", placeholder="A futuristic knight in neon armor...")

if st.button("Generate Image"):
    if not prompt:
        st.warning("Please enter a prompt!")
    else:
        try:
            with st.spinner("Hugging Face is thinking..."):
                image_bytes = query({"inputs": prompt})
                image = Image.open(io.BytesIO(image_bytes))
                
                st.image(image, caption=f"Result for: {prompt}", use_container_width=True)
                st.success("Generated for free!")
        except Exception as e:
            st.error("The model might be 'loading' (cold start). Wait 30 seconds and try again!")
