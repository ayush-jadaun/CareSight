# main.py
from fastapi import FastAPI, UploadFile, File
from emotion import process_emotion
from gaze import process_gaze

app = FastAPI()

@app.post("/detect-emotion")
async def detect_emotion(file: UploadFile = File(...)):
    return await process_emotion(file)

@app.post("/gaze-coordinates")
async def gaaze_coordinates(file: UploadFile = File(...)):
    return await process_gaze(file)
