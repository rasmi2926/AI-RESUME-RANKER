# 📄 AI-Powered Resume Ranker

An AI-powered web application that ranks resumes based on their similarity to a given job description using Natural Language Processing (NLP) and Machine Learning techniques.

## 🚀 Features

- Upload multiple PDF resumes
- Extract text from PDF files
- Clean and preprocess text using SpaCy
- Preprocess job descriptions
- Convert text into numerical vectors using TF-IDF
- Calculate similarity using Cosine Similarity
- Rank resumes based on job description relevance
- Simple and user-friendly Flask web interface

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### Machine Learning & NLP
- Scikit-learn
- SpaCy

### PDF Processing
- PyMuPDF (fitz)

---

## 📂 Project Structure

```
Resume_Ranker/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── images/
│
└── utils/
    ├── pdf_extractor.py
    ├── text_preprocessor.py
    └── ranker.py
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Resume_Ranker.git
cd Resume_Ranker
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Download SpaCy Model

```bash
python -m spacy download en_core_web_sm
```

### 6. Run the Application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 📊 How It Works

1. User uploads one or more resumes in PDF format.
2. User enters a job description.
3. The application extracts text from each resume.
4. Text is cleaned using SpaCy NLP preprocessing.
5. TF-IDF converts resumes and job description into vectors.
6. Cosine Similarity calculates the match score.
7. Resumes are ranked from highest to lowest similarity.

---


## 📦 Requirements

- Python 3.11+
- Flask
- pandas
- numpy
- scikit-learn
- spaCy
- PyMuPDF

---

## 🔮 Future Enhancements

- Resume keyword highlighting
- Skill extraction
- Missing skills analysis
- Resume recommendations
- Export ranking to CSV
- Semantic matching using BERT
- User authentication
- Database integration
- Drag-and-drop resume upload

---

## 👩‍💻 Author

**Rasmi Ranjan Sahu**


---

## 📄 License

This project is developed for educational and internship purposes.
