import streamlit as st 
import pickle
import string 
from nltk.corpus import stopwords
import string 
from nltk.stem.porter import PorterStemmer
import nltk 

ps = PorterStemmer()

def text_tokanize(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    
    
    y =[]
    for i in text:
        if i.isalnum():
          y.append(i)
    text = y[ : ]
    y.clear()
    for i in text :
        if i not in stopwords.words('english') and i not in string.punctuation :
            y.append(i)
    text = y[ : ]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)


tfid = pickle.load(open('vectorize.pkl' ,'rb'))
model = pickle.load(open('model.pkl' ,'rb'))

st.title("Sms-text classifier ")
input_sms = st.text_input("Enter the message ")
if st.button("Predict"):
    #1 preprocessing 
    Transform_sms = text_tokanize(input_sms)

    #2 vectorized 
    vecotize_sms=tfid.transform([Transform_sms])

    #3 predict
    Result = model.predict(vecotize_sms)[0]

    #4 Result 
    if Result == 1:
        st.header("Spam")
    else :
        st.header("not spam")