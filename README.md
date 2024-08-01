# ATS Resume Expert

## Overview

ATS Resume Expert is a web application built using Streamlit that parses resumes from PDF files and converts them into JSON format. The application uses Google Gemini API for processing and analyzing the resume content. This tool helps in transforming resumes into structured JSON data for easier integration and analysis.

## Features

- **PDF Upload**: Upload your resume in PDF format.
- **Resume Parsing**: Extracts and converts resume content into a structured JSON format.
- **JSON Output**: Displays the parsed resume in a readable JSON format.

## Technologies Used

- **Streamlit**: For creating the web interface.
- **PyMuPDF (fitz)**: For extracting images from PDF files.
- **Pillow (PIL)**: For handling image data.
- **Google Gemini API**: For generating content and parsing the resume.
- **dotenv**: For managing environment variables.

## Installation

To run the application, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ats-resume-expert.git
   cd ats-resume-expert
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your Google API key:

   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

## Usage

1. **Upload Resume**: Click on the "Upload your resume (PDF)..." button and select a PDF file of your resume.
2. **Parse Resume**: Click on the "Parse Resume to JSON" button to process the resume and get it in JSON format.
3. **View Output**: The parsed resume will be displayed in JSON format on the web page.

## Prompt Used

The following prompt is used to instruct the Google Gemini API to parse the resume content and provide it in JSON format:

```plaintext
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
```

## Troubleshooting

- **Error Parsing JSON**: If the application fails to parse the JSON, ensure the response from the API is valid and properly formatted.
- **PDF Processing Issues**: Ensure the PDF is not encrypted and contains the expected content.

## Contributing

Feel free to open issues or submit pull requests to contribute to the project. Ensure to follow best practices for code quality and documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
