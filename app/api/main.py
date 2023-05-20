import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from urllib import request
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Zoo Animal CLassification",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

IMG_SIZE = (100,100)

model = tf.keras.models.load_model("saved_model/trained_model")

animal_classes = {
    0: "cane",
    1: "cavallo",
    2: "elefante",
    3: "farfalla",
    4: "gallina",
    5: "gatto",
    6: "mucca",
    7: "pecora",
    8: "ragno",
    9: "scoiattolo",
}

@app.get("/")
def read_root(text: str = ""):
    if not text:
        return f"Try to append ?text=something in the URL!"
    else:
        return text


# /predict/?URL=https://www.gallina.it/gallina.jpg
@app.get("/predict/")
def predict(URL) -> str:
    with request.urlopen(URL) as url:
        img = image.load_img(BytesIO(url.read()), target_size=IMG_SIZE)

    img_array = image.img_to_array(img) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_batch)
    return animal_classes[int(prediction.argmax(axis=-1))]
