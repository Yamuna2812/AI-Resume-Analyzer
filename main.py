import streamlit as st
from utils import extract_text, get_similarity, get_missing_skills, get_ai_feedback

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):
    if uploaded_file and job_desc:
        with st.spinner("Analyzing..."):
            resume_text = extract_text(uploaded_file)

            score = get_similarity(resume_text, job_desc)
            missing = get_missing_skills(resume_text)
            feedback = get_ai_feedback(resume_text)

        st.subheader("📊 Match Score")
        st.success(f"{score}%")

        st.subheader("⚠️ Missing Skills")
        if missing:
            st.write(", ".join(missing))
        else:
            st.write("No major skills missing 🎉")

        st.subheader("🤖 AI Suggestions")
        st.write(feedback)

    else:
        st.warning("Please upload resume and enter job description")



