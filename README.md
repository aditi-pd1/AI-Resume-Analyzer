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

# 1. Clone the repository
git clone https://github.com/aditi-pd1/AI-Resume-Analyzer.git
cd AI-Resume-Analyzer

# 2. (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py


## Usage
1.Open http://127.0.0.1:5000 in your browser.

2.Upload your resume (PDF or DOCX).

3.Paste the job description.

4.Click "Analyze" and view:

✅ TF-IDF Similarity Score

✅ Keyword Match Percentage

✅ Semantic Similarity Score

✅ Matched & Missing Keywords



# 6.Notes
Avoid uploading resumes with scanned images; only text-based PDFs/DOCX are supported.

Make sure en_core_web_md is downloaded for spaCy embeddings.
python -m spacy download en_core_web_md

The tool is designed for educational and portfolio purposes.

# 7.Demo
<img width="902" height="860" alt="Screenshot 2025-07-30 170119" src="https://github.com/user-attachments/assets/7df5aefc-71b7-442d-a991-9f20a566ba9e" />
<img width="926" height="935" alt="Screenshot 2025-07-30 170022" src="https://github.com/user-attachments/assets/63d464e7-2681-4536-b98c-414753ecf830" />

# 8.Folder Structure
AI-Resume-Analyzer/
│
├── app.py                  # Flask backend
├── resume_parser/          # Resume & keyword analysis logic
│   ├── parser.py
│   └── ats_keywords.py
├── utils/
│   └── matcher.py          # TF-IDF similarity logic
├── templates/
│   └── index.html          # Frontend form and results
├── static/
│   └── style.css
├── uploads/                # Temporary resume uploads
├── .gitignore
└── README.md


# 9.License
This project is licensed under the MIT License.
You are free to use, modify, and distribute this software for personal or commercial purposes. See the LICENSE file for more details.
