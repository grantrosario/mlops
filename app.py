import streamlit as st
from model import classify_image

st.title("Image Classifier")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width="always")
    st.write("")
    st.write("Classifying...")
    label, probability = classify_image(uploaded_file)
    st.write(f"Class: {label}, Confidence: {probability:.2f}%")