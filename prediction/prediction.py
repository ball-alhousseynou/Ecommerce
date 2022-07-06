# File: prediction.py
# Author: BALL Alhousseynou
# Date: Tue Jul 05 2022


import joblib
import en_core_web_sm
from preprocessing.preprocessor import (string_to_lower,
                                        preprocessing
                                        )

nlp_spacy = en_core_web_sm.load()
stopwords = nlp_spacy.Defaults.stop_words
stopwords = [string_to_lower(word)
             for word in stopwords]
model = joblib.load("./models/lsvc.joblib")


def predict_lsvc(text: str, nlp_spacy=nlp_spacy, stopwords=stopwords,
                 model=model):
    """
    compute the prediction
    """
    try:
        text_clean = preprocessing(text, nlp_spacy, stopwords)
        y_pred = model.predict([text_clean])
        return y_pred[0]

    except Exception:
        print("Input non valid. Merci d'entrer du text")


# text = ("Paper Plane Design Framed Wall Hanging Motivational Office "
#         "Decor Art Prints (8.7 X 8.7 inch) - Set of 4 Painting made "
#         "up in synthetic frame with uv textured print which gives multi "
#         "effects and attracts towards it. This is an special series of "
#         "paintings which makes your wall very beautiful and gives a royal "
#         "touch. This painting is ready to hang, you would be proud to "
#         "possess this unique painting that is a niche apart. We use only "
#         "the most modern and efficient printing technology on our prints, "
#         "with only the and inks and precision epson, roland and hp printers."
#         "This innovative hd printing technique results in durable and "
#         "spectacular looking prints of the highest that last a lifetime. "
#         "We print solely with top-notch 100% inks, to achieve brilliant "
#         "and true colours. Due to their high level of uv resistance, our "
#         "prints retain their beautiful colours for many years. Add colour "
#         "and style to your living space with this digitally printed painting"
#         "Some are for pleasure and some for eternal bliss.so bring home this"
#         "elegant print that is lushed with rich colors that makes it nothing"
#         "but sheer elegance to be to your friends and family.it would be "
#         "treasured forever by whoever your lucky recipient is. "
#         "Liven up your place with these intriguing paintings that "
#         "are high definition hd graphic digital prints for home, "
#         "office or any room.")
