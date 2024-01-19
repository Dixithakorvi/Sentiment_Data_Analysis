# IMDb Review Sentiment Analysis Application

This repository contains the code for a machine learning web application that performs sentiment analysis on IMDb movie reviews. The application is built with Streamlit and deployed on Heroku.

## Overview

The application uses a Logistic Regression model trained on the IMDb dataset to predict whether a given movie review has a positive or negative sentiment. Users can enter a movie review into the web interface, and the model will classify the sentiment as either positive or negative.

## Repository Structure
`sentiment_app.py`: Streamlit application script.
  `your_model.joblib`: Serialized model file used for predictions.  
  `Procfile`: Heroku deployment commands. 
  `setup.sh`: Configuration for setting up the Streamlit environment on Heroku.
  `requirements.txt`: Required Python packages.
    `runtime.txt`: Specifies the Python runtime version.
     `IMDB Dataset.csv`: Dataset used for training the model.
    `Model.ipynb`: Jupyter notebook with the model training code. 
     `enhanced_sentiment_model.pkl`: Original serialized model file.
     
## To run Application in local machine
1. Clone the repository.
2. Ensure you have Python 3.7+ installed.
3. Install the requirements using `pip install -r requirements.txt`.
4. Run the app with `streamlit run sentiment_app.py`.

## Using the Application
>URL- https://imdbsentimentanalysis-c098a9d5d21f.herokuapp.com/ 
-   Visit the live URL or run the app locally. 
-   Enter an IMDb movie review in the text box such as "Amazing" or "Bad movie".
-   Click 'Analyze' to see the sentiment prediction.
