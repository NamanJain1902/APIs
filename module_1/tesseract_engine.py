import pytesseract


class TesseractEngine:

    def __init__(self):
        pass

    def img2txt(self, img, language='eng'):
        return pytesseract.image_to_string(img, lang = language)