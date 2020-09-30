import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion, make_pipeline
from sklearn.preprocessing import FunctionTransformer, StandardScaler


def _get_text_length(x):
    return np.array([len(t) for t in x]).reshape(-1, 1)


def get_features():
    tfidf_vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(1, 1))

    length_pipe = make_pipeline(
        FunctionTransformer(_get_text_length, validate=False),
        StandardScaler(with_mean=False),
    )

    return FeatureUnion(
        [
            ("text", tfidf_vectorizer),
            ("length", length_pipe),
        ]
    )
