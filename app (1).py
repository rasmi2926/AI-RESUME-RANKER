from flask import Flask, render_template, request
import os

from utils.pdf_extractor import extract_text_from_pdf
from utils.text_preprocessor import preprocess_text
from utils.ranker import rank_resumes

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    # Get uploaded resumes
    files = request.files.getlist("resumes")

    # Get and preprocess job description
    job_description = request.form["job_description"]
    job_description = preprocess_text(job_description)

    resume_texts = []

    # Process each uploaded resume
    for file in files:

        if file.filename != "":

            file_path = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(file_path)

            # Extract text from PDF
            text = extract_text_from_pdf(file_path)

            # Clean the extracted text
            clean_text = preprocess_text(text)

            resume_texts.append({
                "filename": file.filename,
                "text": clean_text
            })

    # Rank resumes
    ranked_resumes = rank_resumes(
        job_description,
        resume_texts
    )

    # Display results
    output = "<h1>Resume Ranking</h1>"

    for resume in ranked_resumes:

        output += f"""
        <h3>{resume['filename']}</h3>
        <h2>Match Score: {resume['score']}%</h2>
        <hr>
        """

    return output


if __name__ == "__main__":
    app.run(debug=True)