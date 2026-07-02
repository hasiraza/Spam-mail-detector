import streamlit as slt
from config import model, vectorizer
from utils import transformation
import time

slt.set_page_config(page_title="Spam Mail Detector")
slt.title("Spam Mail Detector")

with slt.sidebar:
    slt.header("About Developer")
    slt.write("Muhammad Haseeb")

    slt.markdown("📧 Gmail: hasiraza511@gmail.com")
    slt.markdown("💼 LinkedIn: https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/")

    slt.divider()

    slt.header("Downloads")
    with open("artifacts.zip", "rb") as f:
        slt.download_button(
            "Download Project Files",
            f,
            "artifacts.zip"
        )

text = slt.text_area("Enter your email")

if slt.button("Check"):
    if text.strip():
        with slt.spinner("Analyzing email..."):
            transformed = transformation(text)
            vectorized = vectorizer.transform([transformed])
            prediction = model.predict(vectorized)
            time.sleep(1)

        if prediction[0] == 1:
            slt.error("Spam detected")
        else:
            slt.success("Not spam")
    else:
        slt.warning("Please enter an email")