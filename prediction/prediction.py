# File: prediction.py
# Author: BALL Alhousseynou
# Date: Tue Jul 05 2022


import joblib
import pandas as pd
lsvc_model = joblib.load("./models/lsvc.joblib")


def predict_lsvc(text: str):
    """
    compute the prediction with lsvc
    """
    try:
        y_pred = lsvc_model.predict(pd.Series(text))
        return y_pred[0]

    except Exception:
        print("Input non valid. Merci d'entrer du text")


def predict_bert(text: str,
                 model_path="./models/bert.onnx"):
    """
    compute the prediction with bert
    """
    return None


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
