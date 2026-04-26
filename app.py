import streamlit as st
import random

st.set_page_config(page_title="AI Art Generator", page_icon="🖼️")
st.title("🖼️ Ultra-Stable Art Bot")
st.write("If an image doesn't show up, just click 'Generate' again!")

# 1. Get the User Prompt
prompt = st.text_input("What do you want to see?", placeholder="A futuristic castle...")

if st.button("Generate Image"):
    if prompt:
        # The Secret Sauce: A random number forces the server to try harder
        seed = random.randint(1, 9999999)
        
        # We use a slightly different URL structure that is more stable in 2026
        # Adding 'turbo=true' helps prioritize your request
        image_url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?seed={seed}&width=1024&height=1024&nologo=true&turbo=true"
        
        with st.spinner("🎨 AI is painting your masterpiece..."):
            # We display the image
            st.image(image_url, caption=f"Result for: {prompt}", use_container_width=True)
            
            # This 'Download' link also acts as a backup in case the display fails
            st.markdown(f"🔗 [Direct Image Link]({image_url})")
            st.info("Tip: If the image above is blank, wait 3 seconds and click Generate again.")
    else:
        st.warning("Please type something first!")
