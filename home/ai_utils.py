from transformers import pipeline

# Load the sentiment analysis pipeline with the chosen model
classifier = pipeline(
    "sentiment-analysis", 
    model="distilbert-base-uncased-finetuned-sst-2-english",
    framework="pt"  # <--- Force PyTorch backend
)

def predict_priority(text):
    """
    Predicts task priority based on sentiment.
    Positive => Low
    Neutral => Medium (if available)
    Negative => High
    """
    # Get sentiment analysis result
    result = classifier(text)[0]
    label = result['label']

    # Mapping sentiment to task priority
    if label == "POSITIVE":
        return "Low"
    elif label == "NEGATIVE":
        return "High"
    else:
        return "Medium"
    
def predict_priority(text):
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    result = classifier(text)[0]
    ...

