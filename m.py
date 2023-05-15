import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import nltk
#import itertools
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

from nltk.corpus import wordnet
import joblib
import fastparquet

#nltk.download('punkt')
#nltk.download('stopwords')

#app = FastAPI()
print("Hola")
#Importamos archivos y modelos
df = pd.read_csv('./DataSet/movies_dataset_normalizado.csv' )
modelo_entrenado = joblib.load("./DataSet/prediccion_rl.plk")
df_predic = pd.read_parquet("./DataSet/token.parquet")
print("Hola")