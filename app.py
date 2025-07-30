from resume_parser.parser import extract_resume_text
from resume_parser.ats_keywords import get_keyword_matches
from utils.matcher import calculate_similarity
from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    resume_file = request.files['resume']
    job_description = request.form['job_description']

    if resume_file:
        filename = resume_file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)
        resume_text = extract_resume_text(filepath)
        print("Extracted Resume Text:\n", resume_text[:500])  # Optional: for debugging

        # TF-IDF similarity
        similarity = calculate_similarity(resume_text, job_description)

        # Keyword and semantic analysis
        keyword_analysis = get_keyword_matches(resume_text, job_description)
        matched = keyword_analysis["matched_keywords"]
        missing = keyword_analysis["missing_keywords"]
        keyword_score = keyword_analysis["keyword_match_percent"]
        semantic_score = keyword_analysis["semantic_similarity_percent"]
        composite_score = round((0.3 * similarity) + (0.3 * keyword_score) + (0.4 * semantic_score), 2)

        result = f"""
        <strong>Resume parsed successfully.</strong><br><br>
        <b>TF-IDF Similarity Score:</b> {similarity}%<br>
        <b>Keyword Match Score:</b> {keyword_score}%<br>
        <b>Semantic Similarity Score:</b> {semantic_score}%<br><br>
        <b style='color: green;'>Composite Match Score:</b> {composite_score}%<br><br>
        <strong>Matched Keywords:</strong> {', '.join(matched)}<br><br>
        <strong>Missing Keywords:</strong> {', '.join(missing)}
        """

        return render_template('index.html', result=result)

    return render_template('index.html', result="No file uploaded.")

# ✅ Correct __name__ block
if __name__ == '__main__':
    app.run(debug=True)
