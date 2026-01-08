📄 AI Resume Skill Matcher 

A simple AI-powered Resume Skill Matcher that compares a resume with a job description, calculates a match percentage, and highlights matched and missing skills. Inspired by basic Applicant Tracking Systems (ATS).

🚀 Features

Compare resume and job description text

Calculate match percentage using TF-IDF and cosine similarity

Identify matched skills and missing skills

Curated skill list ensures relevant technical skills only

Built with Python and Streamlit for an interactive UI

🛠️ Tech Stack

Python – core programming

Streamlit – for web app UI

Scikit-learn (TF-IDF & cosine similarity) – for text vectorization and similarity calculation

Regex – text cleaning

💡 How It Works

Text Cleaning – Converts text to lowercase and removes punctuation.

TF-IDF Vectorization – Transforms resume and job description into numerical vectors.

Cosine Similarity – Computes similarity score between vectors for match percentage.

Skill Matching – Compares resume text with a curated skill dictionary to find matched and missing skills.

📋 Sample Usage

Resume Input:

I am a data science student with skills in Python, Pandas, NumPy, and Matplotlib. 
I have experience in data analysis, machine learning, and statistics.


Job Description Input:

Looking for a Data Analyst with Python, SQL, Pandas, NumPy, data visualization, 
and experience in dashboards and reporting.


Output:

✅ Match Percentage: 52.72%

✅ Matched Skills: python, pandas, numpy, data analysis, matplotlib, statistics

❌ Missing Skills: sql, data visualization, dashboards, reporting

📦 Installation

Clone the repository:

git clone https://github.com/ujwalta/ATS_Resume_Skill_Matcher.git
cd ATS_Resume_Skill_Matcher


Install dependencies:

pip install streamlit scikit-learn


Run the app:

streamlit run app.py

📌 Notes

The project uses a curated skill dictionary to filter out irrelevant words.
TF-IDF is used for similarity calculation, but this can be upgraded to embedding-based methods for semantic matching.
Ideal for learning NLP basics and ATS-style resume matching.

TF-IDF is used for similarity calculation, but this can be upgraded to embedding-based methods for semantic matching.

Ideal for learning NLP basics and ATS-style resume matching.
