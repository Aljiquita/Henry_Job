import pandas as pd
import datetime as dt
import numpy as np
from datetime import datetime
from fastapi import FastAPI
import fastparquet
import nltk
import re


from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

data_set_EDA = pd.read_parquet("./DataSet/data_set_EDA.parquet")

def listar_titulo_sin_lematizar(titulo: str):
    # Le vamos aplicando la Normalizacion y luega el Stemming al titulo
    palabra = titulo
    # Tokenizamos para separar las palabras del titular
    palabra= nltk.word_tokenize(palabra)
    # Eliminamos las palabras de menos de 3 letras
    palabra = [palabra for palabra in palabra if len(palabra)>2]
    return palabra
#print(listar_titulo_sin_lematizar("Toy Story Collection"))


    

