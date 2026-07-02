import zipfile

with zipfile.ZipFile("artifacts.zip", "w") as zipf:
    zipf.write("model/model.pkl")
    zipf.write("model/vectorizer.pkl")