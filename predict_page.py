import streamlit as st
import pandas as pd
import string

import nltk
# nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

import pickle


def load_model():
    with open('model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

# Get the trained model and vectorizer
clf = data["model"]
vectorizer = data["vectorizer"]



###################################################
###############  Helper Functions  ################
###################################################
def tag(review_without_stopwords):
    return TextBlob(review_without_stopwords).tags


stop = stopwords.words('english')
def remove_stop_words(col):
    new_col = []
    for review in col:
        new_val = []
        review = review.translate(str.maketrans('', '', string.punctuation))
        for word in review.split():
            if word not in stop:
                new_val.append(word)
        new_col.append(' '.join(new_val))
    return new_col


def reformat_tagged_words(col):
    new_col = []
    for review in col:
        new_val = []
        for tagged_tuple in review:
            new_val.append("/".join(tagged_tuple))
        new_col.append(' '.join(new_val))
    return new_col



###################################################
#################  Main Function  ################
###################################################
def show_predict_page():
    st.title("Predicting Reliability of Hotel Reviews")
    st.write("""#### Please enter a hotel review in plain text. The system will classify the review as truthful or deceptive.""")
    st.write("""##### Note: the current trained model has an accuracy of 88.125%.""")

    user_input = st.text_area("Hotel Review (in plain text)", "") # no default values
    df = pd.DataFrame([user_input], columns =['review'])
    df['review_without_stopwords'] = remove_stop_words(df['review'])

    # Add tags to reviews
    tagged_arr = df.review_without_stopwords.apply(tag)
    temp = pd.DataFrame(tagged_arr)

    # Convert each array to string
    df['tagged_review'] = reformat_tagged_words(temp['review_without_stopwords'])

    if st.button("Generate Result"):
        X = vectorizer.transform(df['tagged_review'])
        result = clf.predict(X) # call the exported model
        st.subheader(f"The hotel review is {result[0]}.")
