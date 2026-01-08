import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

# --------------------------------------------------
# Skill Dictionary (Curated, Real Skills Only)
# --------------------------------------------------
SKILLS = {
    "python", "sql", "pandas", "numpy", "matplotlib",
    "scikit-learn", "machine learning", "statistics",
    "data analysis", "eda", "data visualization",
    "dashboards", "reporting", "deep learning",
    "tensorflow", "pytorch", "excel", "power bi"
}

# --------------------------------------------------
# Helper Functions
# --------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def extract_skills(text):
    found_skills = set()
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)
    return found_skills

# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.set_page_config(page_title="AI Resume Skill Matcher", page_icon="📄")

st.title("📄 AI Resume Skill Matcher")
st.write("A simple ATS-style tool using NLP (TF-IDF) to compare resumes and job descriptions.")

resume_text = st.text_area("📌 Paste Resume Text", height=220)
job_text = st.text_area("📌 Paste Job Description", height=220)

if st.button("🔍 Analyze Match"):
    if resume_text.strip() == "" or job_text.strip() == "":
        st.warning("⚠️ Please paste both resume and job description.")
    else:
        # Clean text
        resume_clean = clean_text(resume_text)
        job_clean = clean_text(job_text)

        # --------------------------------------------------
        # Similarity Score using TF-IDF
        # --------------------------------------------------
        vectorizer = TfidfVectorizer(stop_words="english")
        vectors = vectorizer.fit_transform([resume_clean, job_clean])

        similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        match_percentage = round(similarity_score * 100, 2)

        # --------------------------------------------------
        # Skill Extraction
        # --------------------------------------------------
        resume_skills = extract_skills(resume_clean)
        job_skills = extract_skills(job_clean)

        matched_skills = resume_skills.intersection(job_skills)
        missing_skills = job_skills.difference(resume_skills)

        # --------------------------------------------------
        # Results
        # --------------------------------------------------
        st.subheader("📊 Match Result")
        st.success(f"✅ Match Percentage: {match_percentage}%")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matched Skills")
            if matched_skills:
                st.write(", ".join(sorted(matched_skills)))
            else:
                st.write("No matched skills found.")

        with col2:
            st.subheader("❌ Missing Skills")
            if missing_skills:
                st.write(", ".join(sorted(missing_skills)))
            else:
                st.write("No missing skills. Strong profile match!")

        st.info(
            "ℹ️ This project uses TF-IDF for similarity and a curated skill dictionary "
            "to simulate a basic Applicant Tracking System (ATS)."
        )
