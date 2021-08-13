import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of  course reviews.", classes="text-h1 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text = "Theese graphs represent course review analysis.")


    return wp


jp.justpy(app)