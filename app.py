import streamlit as st
import requests
import io
from PIL import Image
import random

st.set_page_config(page_title="Instant AI Art", page_icon="🎨")
st.title("🎨 Instant AI Image Bot")
st.write("No keys. No waiting. Just art.")

prompt = st.text_input("What should the AI draw?", placeholder="A futuristic city in the rain...")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("AI is painting..."):
            # We add a random seed so it generates a new image every time
            seed = random.randint(0, 999999)
            
            # This is the Pollinations API URL - it's fast and free
            image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed}&width=1024&height=1024&nologo=true"
            
            try:
                # We fetch the image from the URL
                response = requests.get(image_url)
                if response.status_code == 200:
                    image = Image.open(io.BytesIO(response.content))
                    st.image(image, use_container_width=True)
                    st.success("Boom! There it is.")
                else:
                    st.error("The art server is a bit busy, try again in 5 seconds!")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
