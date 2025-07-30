# AI-Resume-Analyzer

AI Resume Analyzer is a smart web-based tool that compares a candidate’s resume with a job description using Natural Language Processing (NLP). It provides an ATS (Applicant Tracking System) compatibility score, keyword match percentage, and semantic similarity score to help improve your resume for job applications.

---

##  Features

- ✅ Resume parsing from PDF or DOCX
- ✅ Extracts and compares keywords from resume and JD
- ✅ Calculates:
  - TF-IDF similarity score
  - Keyword match percentage
  - Semantic similarity using spaCy embeddings
- ✅ Synonym-aware keyword matching (e.g., "ML" = "machine learning")
- ✅ Visual results with matched and missing keywords
- ✅ Simple web interface using Flask

---

##  Tech Stack

- **Frontend**: HTML, CSS (vanilla)
- **Backend**: Python (Flask)
- **NLP & ML**: spaCy, scikit-learn, NLTK
- **Other Libraries**: pdfminer, python-docx

---

##  Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

