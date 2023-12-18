import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set Streamlit app title and sidebar layout
st.set_page_config(page_title="Image Generator", layout="wide")

# Main title
st.title("Image Generator")

# Prompt input
prompt = st.text_input("Enter a prompt")

# Generate button
if st.button("Generate Image"):
    if prompt:
        # Generate the image
        response = openai.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        # Display the generated image
        image_url = response.data[0].url
        st.image(image_url, use_column_width=True)
    else:
        st.warning("Please enter a prompt")

# Add custom CSS for footer
footer_style = """
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
padding: 10px;
background-color: #f5f5f5;
"""
# Footer
st.markdown(
    '<div style="{}">Developed by mirac | Contact at: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)