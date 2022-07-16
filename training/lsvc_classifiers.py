# File: ml_classifiers.py
# Author: BALL Alhousseynou
# Date: Thu Jul 07 2022

import pandas as pd
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from joblib import dump
from preprocessing.preprocessor import TextTransformer
import en_core_web_sm
import logging
from config.config_logging import initlogs
initlogs("lsvc_training")
nlp_spacy = en_core_web_sm.load()
stopwords = nlp_spacy.Defaults.stop_words
stopwords = [word.lower() for word in stopwords]


def init_lsvc_model():
    lsvc = Pipeline([("preprocessing", TextTransformer(nlp_spacy, stopwords)),
                     ("tfidf", TfidfVectorizer(lowercase=False,
                                               max_df=0.9,
                                               min_df=3,
                                               ngram_range=(1, 2))),
                     ("clf", LinearSVC())])
    return lsvc


def convert_sklearn(model):
    """
    convert model onnx
    """

    dump(model, "./models/lsvc.joblib")
    logging.info("Model saved!")


def main():
    df = pd.read_csv("./data/ecommerceDataset.csv",
                     names=["labels", "descriptions"])
    descriptions = df["descriptions"].map(str)
    labels = df["labels"]

    x_train, x_test, y_train, y_test = train_test_split(descriptions, labels,
                                                        test_size=0.4,
                                                        stratify=labels,
                                                        random_state=42)
    x_valid, x_test, y_valid, y_test = train_test_split(x_test, y_test,
                                                        test_size=0.5,
                                                        random_state=42)

    model = init_lsvc_model()
    model.fit(x_train, y_train)

    logging.info("metrics validation dataset")
    y_pred = model.predict(x_valid)
    logging.info(classification_report(y_valid, y_pred))

    logging.info("metrics test dataset")
    y_pred = model.predict(x_test)
    logging.info(classification_report(y_test, y_pred))

    convert_sklearn(model)


if __name__ == "__main__":
    main()
