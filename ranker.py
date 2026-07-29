from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def rank_resumes(job_description, resumes):
    """
    Compare each resume with the job description
    and return resumes sorted by similarity score.
    """

    documents = [job_description]

    for resume in resumes:
        documents.append(resume["text"])

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(documents)

    job_vector = vectors[0]

    resume_vectors = vectors[1:]

    scores = cosine_similarity(job_vector, resume_vectors)[0]

    ranked = []

    for i in range(len(resumes)):

        ranked.append({
            "filename": resumes[i]["filename"],
            "score": round(scores[i] * 100, 2)
        })

    ranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return ranked