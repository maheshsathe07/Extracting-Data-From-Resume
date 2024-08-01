import os
import io
import base64
import json
import re
from dotenv import load_dotenv
import streamlit as st
import fitz  # PyMuPDF
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google API Key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def get_gemini_response(pdf_content, prompt):
    model = genai.GenerativeModel('gemini-1.5-pro')
    response = model.generate_content([pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
            first_page = pdf_document.load_page(0)
            pix = first_page.get_pixmap()

            img_byte_arr = io.BytesIO()
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save(img_byte_arr, format='JPEG')
            img_byte_arr = img_byte_arr.getvalue()

            pdf_parts = [
                {
                    "mime_type": "image/jpeg",
                    "data": base64.b64encode(img_byte_arr).decode()
                }
            ]
            return pdf_parts
        except Exception as e:
            st.error(f"Error processing PDF: {e}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")

def clean_and_format_json(response_text):
    # Extract JSON content
    json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        # Remove any trailing commas before closing brackets or braces
        json_str = re.sub(r',\s*([}\]])', r'\1', json_str)
        return json_str
    return None

# Streamlit App
st.set_page_config(page_title="Extracting Data From Resume in JSON Format")
st.header("Resume Parser")

uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit = st.button("Parse Resume to JSON")

if submit:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        if pdf_content:
            input_prompt = """
            Parse the content of the resume and convert it into a JSON format. The JSON should include the following fields:

            - Name
            - Contact Information (phone number, email, address)
            - Summary/Objective
            - Skills
            - Experience (company, position, start date, end date, responsibilities)
            - Education (institution, degree, start date, end date)
            - Certifications
            - Projects (name, description, technologies used)
            - Languages
            - Hobbies/Interests

            Provide the output in valid JSON format, enclosed in triple backticks with 'json' specified, like this:
            ```json
            {
                "key": "value"
            }
            ```
            Ensure all JSON is properly formatted and there's no additional text outside the JSON.
            """
            response_text = get_gemini_response(pdf_content, input_prompt)
            
            # Clean and format the response
            cleaned_json_str = clean_and_format_json(response_text)
            
            if cleaned_json_str:
                try:
                    response_json = json.loads(cleaned_json_str)
                    st.subheader("Parsed Resume in JSON")
                    st.json(response_json)
                except json.JSONDecodeError as e:
                    st.error(f"Error parsing JSON. Please try again.")
            else:
                st.error("Unable to extract JSON from the response. Please try again.")
        else:
            st.write("Please upload a valid resume")
    else:
        st.write("Please upload the resume")