from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


def get_pipeline(features):
    classifier = MultinomialNB()
    return Pipeline([("features", features), ("clf", classifier)])
