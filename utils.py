import pdfplumber
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Extract text from PDF
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

# Calculate similarity
def get_similarity(resume, job_desc):
    tfidf = TfidfVectorizer()
    vectors = tfidf.fit_transform([resume, job_desc])
    score = cosine_similarity(vectors[0], vectors[1])
    return round(score[0][0] * 100, 2)

# Skill matching
skills_list = [
    "python", "machine learning", "sql", "data analysis",
    "ai", "deep learning", "nlp", "communication", "excel"
]

def get_missing_skills(resume):
    resume = resume.lower()
    missing = [skill for skill in skills_list if skill not in resume]
    return missing

# AI feedback
def get_ai_feedback(resume):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Analyze this resume and give clear improvement suggestions:\n{resume}"
                }
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"
    


from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

