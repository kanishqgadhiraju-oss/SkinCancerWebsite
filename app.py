import streamlit as st
from PIL import Image

st.title("Skin Cancer Detection AI")
st.write("Science Fair Demo: Upload a skin image below:")

uploaded_file = st.file_uploader("Upload a skin image", type=["jpg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Placeholder for AI predictions
    st.write("Risk Level: [Prediction will appear here]")
    st.write("Advice: [Advice will appear here]")
