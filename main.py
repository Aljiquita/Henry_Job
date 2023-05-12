import pandas as pd
import datetime as dt
from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Text, Optional
from uuid import uuid4 as uui
import numpy as np

 


app = FastAPI()

df = pd.read_csv('./DataSet/movies_dataset_normalizado.csv' )

df["release_date"] = pd.to_datetime(df["release_date"])
df["release_month_name"] = df["release_date"].dt.month
mes_letras= [
    df["release_month_name"] == 1,
    df["release_month_name"] == 2,
    df["release_month_name"] == 3,
    df["release_month_name"] == 4,
    df["release_month_name"] == 5,
    df["release_month_name"] == 6,
    df["release_month_name"] == 7,
    df["release_month_name"] == 8,
    df["release_month_name"] == 9,
    df["release_month_name"] == 10,
    df["release_month_name"] == 11,
    df["release_month_name"] == 12
]
opciones_mes_letras = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
df["release_month_name"] = np.select(mes_letras, opciones_mes_letras)



# A-) def peliculas_mes(mes): 
@app.get("/peliculas_mes/{mes}")
def peliculas_mes(mes: str):
    '''Se ingresa el mes y la función retorna la cantidad de películas que se estrenaron ese mes históricamente'''
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_month_name"] = df['release_date'].dt.month_name()#locale='es'
    respuesta = df["release_month_name"][df["release_month_name"] == mes].count()
    if respuesta > 0:
        return {'mes':mes, 'cantidad': f"{respuesta}"  }
    return "Valor invalido.. Ej (enero) "



# B-) def peliculas_dia(dia): 
@app.get("/peliculas_dia/{dia}")
def peliculas_dia(dia: str):
    '''Se ingresa el dia y la función retorna la cantidad de peliculas que se estrenaron ese dia históricamente'''
    
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["release_day_name"] = df['release_date'].dt.day_name()#locale='es'
    respuesta = df["release_day_name"][df["release_day_name"]== dia].count()
    if respuesta > 0:
        return {'dia':dia, 'cantidad':f"{respuesta}"}
    return "Valor invalido.. Ej (Monday)"


# C-) def franquicia(franquicia): 
@app.get("/franquicia/{franquicia}")
def franquicia(franquicia: str):
    '''Se ingresa la franquicia, retornando la cantidad de peliculas, ganancia total y promedio'''
    ft = df["belongs_to_collection"][df["belongs_to_collection"].str.contains(franquicia)]
    gt = df["revenue"][df["belongs_to_collection"].str.contains(franquicia)]
    if ft.count() > 0:
        return {'franquicia': f"{franquicia}", 'cantidad': f"{ft.count()}", 'ganancia_total': f"{gt.sum()}", 'ganancia_promedio': f"{gt.sum()/ft.count()}"}
    return "Nombre de Francia no Existente"


# D-) def peliculas_pais(pais): 
@app.get("/peliculas_pais/{pais}")
def peliculas_pais(pais: str):
    '''Ingresas el pais, retornando la cantidad de peliculas producidas en el mismo'''
    pp = df["production_countries"][df["production_countries"].str.contains(f"{pais}")]
    if pp.count() > 0:
        return   {'pais':pais, 'cantidad': f"{pp.count()}"}
    return "País No Existente"


# E-) def productoras(productora): 
@app.get("/productoras/{productoras}")
def productoras(productora: str):
    '''Ingresas la productora, retornando la ganancia total y la cantidad de peliculas que produjeron'''
    pt = df["production_companies"][df["production_companies"].str.contains(f"{productora}")]
    ptg = df["revenue"][df["production_companies"].str.contains(f"{productora}")]
    if pt.count() > 0:
        return {'productora':productora, 'ganancia_total': f"{ptg.sum()}", 'cantidad': f"{pt.count()}"}
    return "Productora No Existente"


# F-) def retorno(pelicula): 
@app.get("/retorno/{pelicula}")
def retorno(pelicula):
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    plRet = df["return"][(df["title"] == f"{pelicula}") & (df["return"] > 0) ]
    if plRet.count() > 0:
        plGan = df["revenue"][(df["title"] == f"{pelicula}") & (df["return"] > 0) ]
        plInv = df["budget"][(df["title"] == f"{pelicula}") & (df["return"] > 0) ]
        anio = df["release_year"][(df["title"] == f"{pelicula}") & (df["return"] > 0) ]
        anio = anio[anio.index[0]]
        return {'pelicula': pelicula, 'inversion': f"{plInv.sum()}", 'ganacia': f"{plGan.sum()}",'retorno': f"{plRet.median()}", 'anio': f"{anio}" }
    return "Datos de Retorno o Película No Existen"

# G-) def recomendacion('titulo'): '''Ingresas un nombre de pelicula y te recomienda las similares en una lista de 5 valores'''
@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    plReco = list(df["title"][df['title'].str.contains(f"{titulo}")])  
    if len(plReco) > 0:
        return  {'lista recomendada': f"{plReco }" }
    return "No se Reporta Este Titulo de Película Relacionado"


@app.get("/get_recommendation/{titulo}")
def get_recommendation(titulo: str):
    df = pd.read_csv("./DataSet/movies_dataset_Para_EDA.csv")
    plReco = df[["title", 'popularity']][df['title'].str.contains(f"{titulo.title()}")]
    plReco = plReco.sort_values(by="popularity", ascending= False)  
    return plReco.head(5)

