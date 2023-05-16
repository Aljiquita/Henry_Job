import pandas as pd
import datetime as dt
import numpy as np
from datetime import datetime
from fastapi import FastAPI
from joblib import load
import fastparquet
import nltk
import re

def listar_titulo_sin_lematizar(titulo: str):
    # Le vamos aplicando la Normalizacion y luega el Stemming al titulo
    palabra = titulo
    # Tokenizamos para separar las palabras del titular
    palabra= nltk.word_tokenize(palabra)
    # Eliminamos las palabras de menos de 3 letras
    palabra = [palabra for palabra in palabra if len(palabra)>2]
    return palabra