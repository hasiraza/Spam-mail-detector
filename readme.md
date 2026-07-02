
# 📧 Spam Mail Detector

A Machine Learning powered spam email detection web application built with Python, Scikit-learn, and Streamlit.

Users can paste email content into the app, and the model predicts whether the email is **Spam** or **Not Spam**.

---

## 🚀 Features

- Detect spam emails instantly
- Text preprocessing using NLTK
- Machine learning classification
- Interactive Streamlit UI
- Download trained model and vectorizer
- Docker support for deployment

---

## 🛠 Tech Stack

- Python 3.12
- Streamlit
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Docker

---

## 📂 Project Structure

```bash
sapm/
│
├── main.py
├── config.py
├── utils.py
├── requirements.txt
├── Dockerfile
├── model.pkl
├── vectorizer.pkl
└── README.md
````

---

## 📊 Machine Learning Pipeline

### Text Preprocessing

* Lowercasing
* Tokenization
* Stopword removal
* Punctuation removal
* Stemming

### Feature Extraction

* CountVectorizer / Bag of Words

### Models Tested

* Multinomial Naive Bayes
* Bernoulli Naive Bayes
* Logistic Regression

---

## Installation

Clone repository:

```bash
git clone <your-repository-url>
cd sapm
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run main.py
```

Open browser:

```bash
http://localhost:8501
```

---

## Docker Setup

Build Docker image:

```bash
docker build -t spam-detector .
```

Run container:

```bash
docker run -p 8501:8501 spam-detector
```

---

## Example Spam Email

```text
Subject: URGENT! Your account has been suspended.
Click the link below to verify your account immediately.
```

---

## Future Improvements

* Deep Learning models
* BERT-based classification
* Email attachment scanning
* API deployment

---

## Contact

### Developer

Muhammad Haseeb

📧 Email: [hasiraza511@gmail.com](mailto:your-email@gmail.com)
💼 LinkedIn: https://www.linkedin.com/in/muhammad-haseeb-raza-71987a366/


---

## License

MIT License

```
```
