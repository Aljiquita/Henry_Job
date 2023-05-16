<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>
<h1 align=center> --PROYECTO INDIVIDUAL Nº1-- </h1>


# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

<h2 align=center> Estudiante: Alberto Jim Quijano Talero </h2>
<h2 align=center> Cohorte: #10 Full Time </h2>


## 1- Transformaciones:  
A- El archivo dispuesto para esta transformación es: Proyecto_DataFrame.ipynb.<br>
B- Pasamos de 45449 filas a 45376.<br>
C- Pasamos de columnas 23 a 18 columnas.<br>
D- El resultado del trabajo realizado de acuerdo a los solicitado por el README para la transformación, se guardo en un nuevo DtaSet llamado "movies_dataset_normalizado.csv" ubicado en la carpeta  "DataSet"<br><br>


## 2- Desarrollo API
A- se encuentra desarrollado su trabajo, organización y prueba de código en el archivo "Desarrollo API".<br>
B- Para el desarrollo de este fase sse tubo en cuenta la importación de Data Set "movies_dataset_normalizado.csv". <br>
C- La API de trabajo ya depurado y lista para subir a render.com, se llama "mani.py".<br>
D- se Genero una cuenta en render.com la cual ya cuenta con la API funcional.<br> 
E- el lik de la API es rende es  https://aljiquita.onrender.com/docs.<br><br>


## 3- Sistema de recomendación:
A- Esta Etapa se desarrollo en el archivo Analisis_exploratorio_datos.ipynb.<br>
B- Para esta etapa del proyecto se realizo un entrenamiento de modelos predictivo.<br>
C- Se utilizo el Data Set "movies_dataset_normalizado.csv".<br>
D- Teniendo el cuenta el requerimiento del proyecto se decidió trabajar con 2 Columnas de datos:<br> 
*   title.<br>
*   vote_average.<br>
E- Después de Normalizada la información para esta nueva etapa del proyecto se genera un nuevo archivo "movies_dataset_Para_EDA.csv" <br><br>


## 4- EDA - Sistema de recomendación:
### En este desarrollo de trabajo ahondaremos un poco mas en la explicación del trabajo
A-  El Archivo donde se trabajo es  "EDA copy.ipynb".<br>
B-  El Data Set Utilizado para esta fase del proyecto fue "movies_dataset_Para_EDA.csv".<br>
C-  Para la preparación de la información se determino asignar como:<br>
*   Data la columna "title" = X
*   la columna "vote_average" = y

D- En la Celda 23 se realiza la depuración de información de la columnas "title", creando una nueva fila de trabajo con el nombre de "title_lemmatizer", con el fin de prepararla para la creación de la data.
*   Se reemplazar los caracteres que no sean leras por espacios.
*   Se pasa todo los textos a minúsculas.
*   Se Tokeniza para separar las palabras del titulo de la películas.
*   Se Aplica un Lemmatizer.
*   Se Eliminan las palabras de menos de 3 letras.
*   Se elimina las palabra que no tienen pesos para el análisis con Stopwords.
*   Se crea una lista con todos los títulos.

F-  Después de Lemmatizada la data se Vectoriza la nueva columna "title_lemmatizer".<br>
G-  Se Divide en el Data Set => title_lemmatizer  y vote_average => values.<br>
H-  Identificamos el koquen con un tamaño de 20824 dentro de un diccionario.<br>
I-  Con el diccionario token creamos un DataFrame el cual lo guardamos como un archivo token.parquet, para posteriormente crear un DataFrame con el cual alimentaremos nuestro modelo de predicción con los nuevos datos.<br>
J-  Se Entrena un Modelo de Predicción con REGRESIÓN LINEAL y un Score del  61%; se guarda el modelo entrenado en el archivo "prediccion_rl.pkl"<br>
K-  Se Entrena un Modelo de Predicción con SMV y un Score del 29.7%; se guarda el modelo entrenado en el archivo "prediccion_SVC.pkl"<br><br>

## 5- Aplicación del modelo Predicción ya entrenado:
A-  El modelo es trabajado en el archivo  "EDA copy.ipyn".<br>
B-  Se crea 3 función para analizar sus trabajo y tomar la decision de utilizar en la IPI un modelo con Regresión Lineal o con SMV:<br>
*   get_recommendation_lr => se pone a prueba el modelo de Regresión Lineal.
*   get_recommendationSVC => se pone a prueba el modelo de SMV. 
*   get_recommendation => Es la función que ira en la API con el modelo seleccionado => Regresión Lineal
c-  Se instala en la API (main.py), con la lamentable citación que al importar el modelo entra en conflicto y no se puede ejecutar.<br>

### NOTA: Al tratar de montar la función "def get_recommendation(titulo: str)",  la importación del modelo es imposible y aunque se intenta con multiples métodos no es exitoso el proceso, curiosamente render permite su ingreso y al ejecutarlo des render o desde un archivo python (.py) no funciona, Pero si se ejecuta desde el Jupyter Notebook la ejecuta a la perfección y la es TODO UN ÉXITO.

D- Se crea un nuevo código para la función get_recommendation con la cual sea posible ejecutarse en la API, trabajado en el archivo "EDA_get_recommendation.ipynb"con las siguientes características:
*   Se tiene encuentra el Dta Set,  Importamos el archivo "movies_dataset_Para_EDA.csv".
*   Normalizamos, depuramos o lematizamos la Data Set en su columnas "title", creando una columna nueva llamada "title_lemmatizer".
* La función toma el nombre de la película y crea un listados de palabra para comparar cada una de las palabras en los títulos de películas para. 

F- Lamentablemente las librerías que que realizan el lematizado de los títulos del las películas crean conflicto con render, por falta de tiempo y experticia en el tema  an solo que pude hacer fue:
*   Tomar el Data Set del archivo "EDA_get_recommendation.ipynb".
*   Tan solo se lista el titulo de la película ingresada en la función.
*   Se busca el listado de palabras del titulo en los la columnas "title" del Data Set

NOTA PERSONA: Fue muy frustrante la experiencia, Debido que en la ultima parte del proyecto realize un Modelo, lo entrene y al final no pude importar a un archivo .py, pero si en un Jupyter Notebook; Después de muchas horas de investigar y trabajas, cree una plan "B" de modelo, el cual lematize los títulos de las películas, pero render fue el problema en este caso, el cual creaba conflicto con las librería necesarias para el lematizado y por estar sobre la fecha limite del tiempo no investigue mas librería que hicieran este mismo trabajo de lematizado; la ultima opción y las sencilla fue listar las palabras del titulo de la pelicula ingresada a la función para posteriormente filtrar los títulos de películas del Data Set.. Repito - FUE MUY FRUSTRANTE ESTE PROYECTO -    


