# File: preprocessor.py
# Author: BALL Alhousseynou
# Date: Tue Jul 05 2022

import pandas as pd
import re
import en_core_web_sm
from functools import partial
from tqdm import tqdm
tqdm.pandas()


def remove_special_chars(text):
    """"
    - remove urls
    - remove html balise
    - remove emails, hastags
    - remove numbers
    - remove words whose length less than 3
    - remove punctuations and others special characters
    """
    text_clean = re.sub(r"http\S+", "", text)
    text_clean = re.sub(r"<.*?>", "", text_clean)
    text_clean = re.sub(r"@|#", "", text_clean)
    text_clean = re.sub(r"[0-9]+", "", text_clean)
    text_clean = re.sub(r"\b\w{1,2}\b", "", text_clean)
    text_clean = re.sub(r"[^A-Za-z0-9]+", " ", text_clean)

    return text_clean.strip()


def string_to_lower(text):
    """
    convert to lower
    """
    return text.lower()


def remove_stops_words(text, nlp_spacy, stopwords):
    """
    remove stops words
    lemmatization
    """
    tokens = nlp_spacy(text)
    return [word.lemma_ for word in tokens
            if (word.text not in stopwords)]


def preprocessing(text, nlp_spacy, stopwords):
    """"
    apply preprocessing
    """
    text_clean = string_to_lower(text)
    text_clean = remove_special_chars(text_clean)
    text_clean = remove_stops_words(text_clean, nlp_spacy, stopwords)
    text_clean = " ".join(text_clean).strip()
    return text_clean


def remove_nan(dataframe, column_name):
    """
    remove nan value from dataframe
    """
    df_clean = dataframe.dropna(subset=[column_name])
    df_clean = df_clean.reset_index()
    return df_clean


def main():
    """
    main function
    """
    nlp_spacy = en_core_web_sm.load()
    stopwords = nlp_spacy.Defaults.stop_words
    stopwords = [string_to_lower(word)
                 for word in stopwords]

    dataframe = pd.read_csv("./data/ecommerceDataset.csv",
                            names=["labels", "descriptions"])
    # dataframe.isna().sum()
    dataframe = remove_nan(dataframe, column_name="descriptions")

    dataframe["descriptions"] = dataframe["descriptions"].map(str)
    p_preprocessing = partial(preprocessing,
                              nlp_spacy=nlp_spacy,
                              stopwords=stopwords)
    dataframe["desc_clean"] = dataframe["descriptions"].progress_apply(
                                                        p_preprocessing)

    dataframe.to_csv("./data/ecommerceDataset_clean.csv", index=False)


if __name__ == "__main__":
    main()
