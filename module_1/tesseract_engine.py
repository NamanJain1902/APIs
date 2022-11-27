import pytesseract


class TesseractEngine:

    def __init__(self):
        pass

    def img2txt(self, img, language='eng'):
        tessdata_dir_config = '--tessdata-dir "/app/.apt/usr/share/tesseract-ocr/4.00/tessdata"'

        return pytesseract.image_to_string(img, lang = language, config=tessdata_dir_config)    
#        return pytesseract.image_to_string(img, lang = language)
