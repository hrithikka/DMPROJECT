#import the required libraries
import streamlit as st
from transformers import pipeline
#Streamlit that allows to enter a text and select a pretrained model
models = ["distilbert-base-uncased-finetuned-sst-2-english", 
          "textblob"]

st.header("Sentiment Analysis App")
sampletext = "I like this course"
tinput = st.text_area("Enter text",value=sampletext)
mselect = st.selectbox("Select a model", models)
#function that performs sentiment analysis using the selected model
def sentiment_analysis(text, mname):
    if mname == "distilbert-base-uncased-finetuned-sst-2-english":
        classifier = pipeline("sentiment-analysis", model=mname)
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
#Call the senitment_analysis function when submit is clicked
if st.button("Submit"):
    result = sentiment_analysis(tinput, mselect)
    st.write("Result:", result)
