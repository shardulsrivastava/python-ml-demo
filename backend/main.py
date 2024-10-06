import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
from PIL import Image
from prediction import predict

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to ECG Intelligence"}

@app.post("/predict")
# def get_prediction(file: UploadFile = File(...)):
def get_prediction():
    predict()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",port=8081)
     