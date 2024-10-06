import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from PIL import Image

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to ECG Intelligence"}

@app.post("/predict")
def get_image(file: UploadFile = File(...)):
    pass

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8080)
    