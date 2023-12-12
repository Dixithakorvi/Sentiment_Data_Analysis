# sentiment_app.py

import streamlit as st
import joblib

# Load the trained model
model = joblib.load('your_model.joblib')

def run_streamlit_app():
    st.title("IMDb Review Sentiment Analysis")
    user_input = st.text_area("Enter a movie review:", "Type your review here...")
    
    if st.button("Analyze"):
        # Make prediction
        prediction = model.predict([user_input])
        sentiment = 'Positive' if prediction[0] == 1 else 'Negative'
        
        # Display the result
        st.write(f"Sentiment: **{sentiment}**")

if __name__ == "__main__":
    run_streamlit_app()
