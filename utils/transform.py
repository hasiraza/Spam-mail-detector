import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

nltk.download('stopwords')
nltk.download('punkt')

stop_words = stopwords.words('english')
ps = PorterStemmer()

def transformation(text):
    # remove Subject:
    text = text.replace("Subject:", "")

    # lowercase
    text = text.lower()

    # tokenize
    tokens = nltk.word_tokenize(text)

    # keep only alphanumeric
    tokens = [word for word in tokens if word.isalnum()]

    # remove stopwords and punctuation
    tokens = [
        word for word in tokens
        if word not in stop_words and word not in string.punctuation
    ]

    # stemming
    tokens = [ps.stem(word) for word in tokens]

    return " ".join(tokens)