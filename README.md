# dse_hackaton

PoC for the Unimi laboratory "Deploy Machine Learning Models on Google Cloud Platform" held by Emanuele Guidotti.
The project uses a self-trained Keras CNN, served by a quick and dirty Streamlit backend, to classify images upload by the user. 
The app is deployed publicly through a Docker Image on a container served by Google Cloud Run.

Dataset used for training: https://www.kaggle.com/datasets/alessiocorrado99/animals10 (10 animals)

### Architecture
![arch](https://github.com/czephyr/dse_hackaton/blob/master/architecture.png?raw=true)

### Demo image
![demo](https://github.com/czephyr/dse_hackaton/blob/master/demo.jpg?raw=true)

### Improvement
A possible improvement was only conceptually explored due to the one-day time constraint the team set. 
In this improvement the problem of monitoring the continuous performance of the model on user input gets addressed;
we added a CloudSQL database, on which inputs and predictions are saved to be assessed in a later moment.
![improv](https://github.com/czephyr/dse_hackaton/blob/master/improvement.png?raw=true)