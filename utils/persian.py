import arabic_reshaper
from bidi.algorithm import get_display


def fa(text: str) -> str:
    """
    نمایش صحیح متن فارسی در Kivy
    """
    reshaped = arabic_reshaper.reshape(text)
    return get_display(reshaped)