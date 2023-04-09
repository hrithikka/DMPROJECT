#import the required libraries
import streamlit as st
from transformers import pipeline
#Streamlit that allows the user to enter a text and select a pretrained model:
models = ["distilbert-base-uncased-finetuned-sst-2-english", 
          "textblob"]

st.header("Sentiment Analysis App")
text_input = st.text_area("Enter text")
model_select = st.selectbox("Select a model", models)
#function that performs sentiment analysis using the selected model:
def analyze_sentiment(text, model_name):
    if model_name == "distilbert-base-uncased-finetuned-sst-2-english":
        classifier = pipeline("sentiment-analysis", model=model_name)
        result = classifier(text)[0]
        return f"label: {result['label']}, score: {result['score']}"
    elif model_name == "textblob":
        from textblob import TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        if polarity > 0:
            return "positive"
        elif polarity < 0:
            return "negative"
        else:
            return "neutral"
#Call the analyze_sentiment function when the user clicks the submit button:
if st.button("Submit"):
    result = analyze_sentiment(text_input, model_select)
    st.write("Result:", result)
