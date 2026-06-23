import streamlit as st
from inference import predict_currency

st.title("💵 Currency Note Recognition")

uploaded = st.file_uploader("Upload a currency note image", type=["jpg","png"])
if uploaded:
    with open("temp.jpg","wb") as f:
        f.write(uploaded.read())
    class_names = ["10 INR","20 INR","50 INR","100 INR","200 INR","500 INR","2000 INR"]
    result = predict_currency("models/currency_model.h5","temp.jpg",class_names)
    st.success(f"Predicted: {result}")
