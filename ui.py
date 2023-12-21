import streamlit as st
import os
import requests
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
         # Get the image URL
        image_url = response.data[0].url

        # Download the image using requests
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # Display the generated image
            st.image(image_url, use_column_width=True)

            # Convert the image response content to a byte stream
            image_bytes = image_response.content

            # Create a download button for the image
            st.download_button(
                label="Download Image",
                data=image_bytes,
                file_name="generated_image.png",
                mime="image/png"
            )
        else:
            st.error("Failed to fetch the image.")
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
background-color: rgba(255, 255, 255, 0.5);  /* Semi-transparent light background */
color: #000;                                  /* Dark text for visibility */
border-top: 1px solid #000;                   /* Border to distinguish the footer */
z-index: 1000;                                /* Ensures it stays on top of other elements */
"""

# Footer
st.markdown(
    '<div style="{}">Developed by Mirac.eth<br>Contact: mirac.eth@ethereum.email</div>'.format(footer_style),
    unsafe_allow_html=True
)
