"""
requirements

fastapi
python-multipart
"""
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import base64
import os


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post('/image_to_text')
def imageToText(filedata: UploadFile = File(...)):
    contents = filedata.file.read()
    from module_1.tesseract_engine import TesseractEngine
    FILE_NAME = "text.png"

    if os.path.exists(FILE_NAME) == False: 
        with open(FILE_NAME, "wb") as fh:
            fh.write(contents)

    tesr_rec_obj = TesseractEngine()
    text_det = tesr_rec_obj.img2txt(FILE_NAME)
    
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    
    return text_det



@app.post('/detect_emotion')
def detectEmotion(filedata: UploadFile = File(...)):
    contents = filedata.file.read()
    import os
    import cv2
    from fer import FER

    FILE_NAME = "face.png"

    if os.path.exists(FILE_NAME) == False: 
        with open(FILE_NAME, "wb") as fh:
            fh.write(contents)

    detector = FER(mtcnn=False)
    emotion, _ = detector.top_emotion(FILE_NAME)
    not_captured = "None"   

    if str(emotion) == not_captured:
        return "Capture Again"
    
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    
    return {"emotion": emotion}

