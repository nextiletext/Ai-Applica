import streamlit as st
import random

st.set_page_config(page_title="AI Art Bot", page_icon="🎨")
st.title("🎨 The Unstoppable Image Bot")
st.write("Generating art using high-speed community servers.")

# 1. Get the User Prompt
prompt = st.text_input("What do you want to see?", placeholder="A cool neon tiger...")

if st.button("Generate Image"):
    if prompt:
        # We create a random seed to make sure every image is unique
        seed = random.randint(0, 999999)
        
        # This is a direct URL to the image generator
        # No API keys, no billing, no age gates.
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed}&width=1024&height=1024&nologo=true"
        
        # 2. Display the image directly using the URL
        # Streamlit handles the 'loading' state automatically here
        with st.spinner("AI is painting... this should only take a few seconds!"):
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            st.success("There it is! No more errors.")
            
            # Optional: Add a download button for the user
            st.markdown(f"[Download Image]({image_url})")
    else:
        st.warning("Type something in the box first!")
