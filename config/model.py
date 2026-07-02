import pickle


with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('model/model.pkl', 'rb') as f:
        model= pickle.load(f)