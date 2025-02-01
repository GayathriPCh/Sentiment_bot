from fastapi import FastAPI
from sentiment_model import analyze_sentiment, roast_review

app = FastAPI()

@app.get("/analyze-sentiment/")
def sentiment(review: str):
    sentiment = analyze_sentiment(review)
    return {"Sentiment": sentiment}

@app.get("/roast-review/")
def roast(review: str):
    roast = roast_review(review)
    return {"Roast": roast}
