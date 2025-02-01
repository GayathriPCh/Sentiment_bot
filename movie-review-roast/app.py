import streamlit as st
import requests

# FastAPI endpoints
API_URL = "http://127.0.0.1:8000"

st.title("Movie Review Sentiment and Roast Generator")
review = st.text_area("Enter your movie review:")

if review:
    # Sentiment analysis
    sentiment_response = requests.get(f"{API_URL}/analyze-sentiment/", params={"review": review})
    sentiment = sentiment_response.json().get("Sentiment")

    # Roast generation
    roast_response = requests.get(f"{API_URL}/roast-review/", params={"review": review})
    roast = roast_response.json().get("Roast")

    st.subheader("Sentiment:")
    st.write(f"The sentiment of the review is: **{sentiment}**")

    st.subheader("Roast:")
    st.write(roast)
