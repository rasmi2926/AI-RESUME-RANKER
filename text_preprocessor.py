import spacy

# Load the English language model only once
nlp = spacy.load("en_core_web_sm")


def preprocess_text(text):
    """
    Clean resume/job description text for NLP.
    """

    doc = nlp(text.lower())

    tokens = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and not token.is_space
        ):
            tokens.append(token.lemma_)

    return " ".join(tokens)