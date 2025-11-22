import joblib
import sys
import streamlit as st

model = joblib.load('phishing_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title('phishing email detector')

st.write("choose how to provide the email content:")

input_method = st.radio(
    "select input method:",
    ('paste email text', 'upload .txt file')

)
email_text = ''

if input_method == 'paste email text':
    email_text = st.text_area('paste email text below:')

elif input_method == 'upload .txt file':
    uploaded_file = st.file_uploader('choose a .txt file', type = 'txt')
    if uploaded_file is not None:
        email_text = uploaded_file.read().decode('utf-8')

if st.button('check email'):
    if email_text.strip() == '':
        st.warning('please provide email text')
    else:
        vectorizer_input = vectorizer.transform([email_text])
        prediction = model.predict(vectorizer_input)
        if prediction[0] == 1:
            st.error('phishing email')
        else:
            st.success('legitimate email')

