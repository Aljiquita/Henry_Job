import pandas as pd
import datetime as dt
import numpy as np
from datetime import datetime
from fastapi import FastAPI
from joblib import load
import fastparquet
import nltk
import re
from nltk.corpus import wordnet

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


stopwords = nltk.corpus.stopwords.words('english')
def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

    

def listar_titulo(titulo: str):
    # Le vamos aplicando la Normalizacion y luega el Stemming al titulo
    palabra = titulo
    # Vamos a reemplzar los caracteres que no sean leras por espacios
    palabra=re.sub("[^a-zA-Z]"," ",str(palabra))
    # Pasamos todo a minúsculas
    palabra=palabra.lower()
    # Tokenizamos para separar las palabras del titular
    palabra= nltk.word_tokenize(palabra)
    # Aplicamos el Lemmatizer (Esto puede tardar un ratito)
    frase_lemma = [wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in palabra]
    # Eliminamos las palabras de menos de 3 letras
    palabra = [palabra for palabra in palabra if len(palabra)>2]
    # Sacamos las Stopwords
    palabra = [palabra for palabra in palabra if not palabra in stopwords]
    # Aplicamos la funcion para buscar la raiz de las palabras
    # palabra=[stemmer.stem(palabra) for palabra in palabra]
    return palabra




def get_recommendation_lema(titulo: str):
    palabra = listar_titulo(titulo)
    plReco = data_set_EDA[["title", "vote_average"]][data_set_EDA['title_lemmatizer'].str.contains('|'.join(palabra))].sort_values("vote_average", ascending= False)
    lis_peli = list(plReco["title"].head(5)) 
    
    return lis_peli