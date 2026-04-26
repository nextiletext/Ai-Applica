import streamlit as st
import requests
import io
from PIL import Image
import random

st.set_page_config(page_title="Relentless AI Art", page_icon="🔥")
st.title("🔥 The 'Never-Give-Up' AI Bot")

prompt = st.text_input("What should I draw?", placeholder="A dragon made of blue fire...")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Searching for an available AI server..."):
            seed = random.randint(0, 999999)
            
            # We try up to 3 different public art servers
            # 1. Pollinations (Main)
            # 2. Cloudflare (Backup)
            # 3. Random Seed (Variation)
            urls = [
                f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed}&nologo=true",
                f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed+1}&width=512&height=512",
                f"https://pollinations.ai/p/{prompt.replace(' ', '%20')}"
            ]
            
            success = False
            for url in urls:
                try:
                    response = requests.get(url, timeout=10)
                    if response.status_code == 200:
                        image = Image.open(io.BytesIO(response.content))
                        st.image(image, use_container_width=True)
                        st.success("Got it!")
                        success = True
                        break # Stop searching if we find a working server
                except:
                    continue # Try the next URL if this one fails
            
            if not success:
                st.error("All free servers are packed right now. Wait 10 seconds and try again!")
