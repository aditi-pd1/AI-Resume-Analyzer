import re
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Ensure NLTK data is downloaded
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Load spaCy model
nlp = spacy.load('en_core_web_md')

# Stopwords and words to ignore
STOPWORDS = set(stopwords.words('english'))
IGNORE_WORDS = STOPWORDS.union({
    'job', 'description', 'title', 'responsibilities', 'required', 'preferred', 'candidate',
    'role', 'apply', 'bonus', 'ideal', 'position', 'qualifications', 'requirement',
    'responsibility', 'writing', 'working', 'structured', 'perform', 'setting', 'report',
    'course', 'completed'
})

# Synonyms dictionary (manually bidirectional)
SYNONYMS = {
    'develop': ['build', 'create', 'design'],
    'build': ['develop'], 'create': ['develop'], 'design': ['develop'],

    'visualization': ['dashboard', 'charts', 'graphs', 'plot'],
    'dashboard': ['visualization'], 'charts': ['visualization'],
    'graphs': ['visualization'], 'plot': ['visualization'],

    'ml': ['machine learning'], 'machine learning': ['ml'],
    'nlp': ['natural language processing', 'text analysis', 'language model'],
    'natural language processing': ['nlp'],
    'text analysis': ['nlp'],
    'language model': ['nlp'],

    'dsa': ['data structures', 'algorithms'],
    'data structures': ['dsa'],
    'algorithms': ['dsa'],

    'cleaning': ['preprocessing', 'wrangling'],
    'preprocessing': ['cleaning'],
    'wrangling': ['cleaning'],

    'python': ['python3', 'python 3'], 'python3': ['python'], 'python 3': ['python'],
    'aws': ['amazon web services'], 'amazon web services': ['aws'],
    'html': ['hypertext markup language'], 'hypertext markup language': ['html'],
    'css': ['cascading style sheets'], 'cascading style sheets': ['css'],
    'sql': ['structured query language'], 'structured query language': ['sql'],
    'js': ['javascript'], 'javascript': ['js'],
    'db': ['database', 'databases'],
    
    'database': ['db'], 'databases': ['db'],
    'intern': ['internship'], 'internship': ['intern'],
    'tf': ['tensorflow'], 'tensorflow': ['tf'],
    'pandas': ['panda'], 'panda': ['pandas'],
    'sklearn': ['scikit', 'scikit-learn'],
    'scikit': ['sklearn'], 'scikit-learn': ['sklearn']
}

lemmatizer = WordNetLemmatizer()

# Text preprocessing
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Lemmatization and filtering
def lemmatize_words(text):
    words = clean_text(text).split()
    return [lemmatizer.lemmatize(word) for word in words if len(word) > 2 and word not in STOPWORDS]

# Expand tokens with synonyms
def expand_with_synonyms(words):
    expanded = set(words)
    for word in list(words):
        if word in SYNONYMS:
            expanded.update(SYNONYMS[word])
    return expanded

# Extract TF-IDF keywords
def extract_keywords(text, top_n=60):
    cleaned = clean_text(text)
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform([cleaned])
    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]
    scored_keywords = list(zip(feature_names, scores))
    sorted_keywords = sorted(scored_keywords, key=lambda x: x[1], reverse=True)
    return set([kw for kw, _ in sorted_keywords[:top_n]])

# Compute semantic similarity using spaCy
def semantic_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return round(doc1.similarity(doc2) * 100, 2)

# Main keyword match function
def get_keyword_matches(resume_text, job_description):
    resume_tokens = lemmatize_words(resume_text)
    jd_tokens = lemmatize_words(job_description)

    resume_tokens = expand_with_synonyms(resume_tokens)
    jd_tokens = expand_with_synonyms(jd_tokens)

    resume_tokens = set([w for w in resume_tokens if w not in IGNORE_WORDS])
    jd_tokens = set([w for w in jd_tokens if w not in IGNORE_WORDS])

    matched = resume_tokens & jd_tokens
    missing = jd_tokens - resume_tokens
    keyword_match_percent = round(len(matched) / len(jd_tokens) * 100, 2) if jd_tokens else 0
    semantic_score = semantic_similarity(resume_text, job_description)

    return {
        "matched_keywords": sorted(matched),
        "missing_keywords": sorted(missing),
        "keyword_match_percent": keyword_match_percent,
        "semantic_similarity_percent": semantic_score,
    }
