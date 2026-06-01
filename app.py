from flask import Flask, render_template, request
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader
import os

#Load environment variables

load_dotenv()

app = Flask(__name__)

#Gemini API Key

api_key = os.getenv(".env")

genai.configure(api_key=api_key)
print("API Key Loaded:", api_key[:5] if api_key else "None")

model = genai.GenerativeModel("gemini-2.0-flash")

def extract_resume_text(pdf_file):
    text = ""

    try:
        reader = PdfReader(pdf_file)

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    except Exception as e:
        text = f"Error reading PDF: {e}"

    return text
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        questions = """
1. Explain OOP concepts in Python.
2. What is the difference between List and Tuple?
3. Explain Flask architecture.
4. How would you optimize a slow database query?
5. Design a scalable interview platform.
"""

        score = 82
        communication = 78
        readiness = 80

        return f"""
        <h1>Generated Interview Questions</h1>
        <pre>{questions}</pre>

        <hr>

        <h2>Interview Analysis</h2>
        <p>Technical Score: {score}/100</p>
        <p>Communication Score: {communication}/100</p>
        <p>Overall Readiness: {readiness}%</p>
        """

    return render_template("index.html")
    score = 82
    communication = 78
    readiness = 80

    return f"""
<h1>Generated Interview Questions</h1>

<pre>{questions}</pre>

<hr>

<h2>Interview Analysis</h2>

<p><b>Technical Score:</b> {score}/100</p>
<p><b>Communication Score:</b> {communication}/100</p>
<p><b>Overall Readiness:</b> {readiness}%</p>

<h3>Strengths</h3>
<ul>
<li>Python</li>
<li>Problem Solving</li>
<li>Flask Development</li>
</ul>

<h3>Areas to Improve</h3>
<ul>
<li>DBMS</li>
<li>System Design</li>
</ul>

<p><b>Recommendation:</b> Interview Ready</p>

<a href="/">Start Again</a>
"""

if __name__ == "__main__":
    app.run(debug=True)