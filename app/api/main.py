import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from io import BytesIO
from urllib import request
from typing import List
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
cwd = os.getcwd()
# st.write(cwd)

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

classes = np.array([animal_classes[i] for i in range(10)])
 
st.write("Upload the image of your animal")
raw_picture = st.file_uploader(label="animal picture")
if raw_picture is not None: 
    st.image(raw_picture)
    img = image.load_img(raw_picture,target_size=IMG_SIZE)

    img_array = image.img_to_array(img) / 255.0
    img_batch = np.expand_dims(img_array, axis=0)
    probs = model.predict(img_batch)[0]
    
    indices = np.argsort(probs)[::-1]
    preds_df = pd.DataFrame(data=zip(classes[indices], probs[indices]), columns=["animal", "probability"])

    fig, ax= plt.subplots(figsize=(10, 5))
    plt.xticks(rotation=45)
    plt.bar(data=preds_df, x="animal", height="probability")
    st.pyplot(fig)
