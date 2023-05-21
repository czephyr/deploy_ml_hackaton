# dse_hackaton

Quick and dirty project for the Unimi laboratory "Deploy Machine Learning Models on Google Cloud Platform" held by Emanuele Guidotti.
The project uses a self-trained Keras CNN, served by a quick Streamlit backend, to classify images upload by the user. 
The app is deployed publicly through a Docker Image on a container served by Google Cloud Run.

Dataset used for training: https://www.kaggle.com/datasets/alessiocorrado99/animals10 (10 animals)

### Architecture
![arch](https://github.com/czephyr/dse_hackaton/blob/master/architecture.png?raw=true)

### Demo image
![arch](https://github.com/czephyr/dse_hackaton/blob/master/photo_2023-05-21_14-49-30.jpg?raw=true)
