import streamlit as st
from openai import OpenAI
import os

# 1. Setup the Webpage Layout
st.set_page_config(page_title="AI Image Generator", page_icon="🎨")
st.title("🎨 AI Image Chatbot")
st.write("Type a description below to generate an image using DALL-E 3.")

# 2. Sidebar for API Key (Keeping it safe!)
with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter OpenAI API Key", type="password")
    st.info("Your key is not stored and is only used for this session.")

# 3. The Generation Logic
prompt = st.text_input("What do you want to see?", placeholder="A futuristic city at sunset...")

if st.button("Generate Image"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar!")
    elif not prompt:
        st.warning("Please enter a prompt first.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            with st.spinner("AI is painting your request..."):
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )

                image_url = response.data[0].url
                st.image(image_url, caption=f"Result for: {prompt}")
                st.success("Done!")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

# 4. Footer
st.markdown("---")
st.caption("Powered by OpenAI DALL-E 3 & Streamlit")
