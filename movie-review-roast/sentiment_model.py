from transformers import pipeline

# Load pre-trained model and tokenizer
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(review):
    result = sentiment_analyzer(review)
    return result[0]['label']

# Function to generate a roast
def roast_review(review):
    sentiment = analyze_sentiment(review)
    if sentiment == 'NEGATIVE':
        return f"Wow, seems like total disaster! 🤦"
    else:
        return f"Looks like somebody got the Hollywood treatment! 🎬"
