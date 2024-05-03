import streamlit as st
from deep_translator import GoogleTranslator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_sentiment(poem):
    translated_text = GoogleTranslator(source='auto', target='en').translate(poem)
    analyzer = SentimentIntensityAnalyzer()
    sentiment_dict = analyzer.polarity_scores(translated_text)
    
    st.write("\nTranslated Poem:", translated_text)
    st.write("Dictionary:", sentiment_dict)
    
    if sentiment_dict['compound'] >= 0.6:
        st.write("Sentiment: Motivational", unsafe_allow_html=True)
    elif 0.3 <= sentiment_dict['compound'] < 0.6:
        st.write("Sentiment: Inspirational", unsafe_allow_html=True)
    elif -0.1 <= sentiment_dict['compound'] < 0.1:
        st.write("Sentiment: Open-minded", unsafe_allow_html=True)
    elif -0.6 <= sentiment_dict['compound'] < -0.1:
        st.write("Sentiment: Sad", unsafe_allow_html=True)
    else:
        st.write("Sentiment: Depressing", unsafe_allow_html=True)

st.title("Sentiment Analysis")

uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
if uploaded_file is not None:
    poem = uploaded_file.read().decode("utf-8")
    analyze_sentiment(poem)
