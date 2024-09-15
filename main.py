from fastapi import FastAPI
from typing import Union
import pandas as pd

app = FastAPI()

data_movies = pd.read_csv("movies_dataset_modified.csv")
data_credits = pd.read_csv("credits_dataset_modified.csv")

@app.get("/Cantidad Filmaciones Mes")
def cantidad_filmaciones_mes(mes: str):
    conteo_meses = len(data_movies[data_movies['month'] == mes])
    return f"{conteo_meses} son la cantidad de películas que han sido estrenadas en el mes de {mes}"


@app.get("/Cantidad Filmaciones Dia")
def cantidad_filmaciones_dia(dia: str):
    conteo_dias = len(data_movies[data_movies['day'] == dia])
    return f"{conteo_dias} son la cantidad de películas que han sido estrenadas en el día de {dia}"


@app.get("/Score Titulo")
def score_titulo(titulo_filmacion: str):
    for i in data_movies['title']:
        if i == titulo_filmacion:
            valores = data_movies[data_movies['title'] == i]
            break

    lista_pelicula = valores['title'].to_string().split()
    pelicula = ' '.join(lista_pelicula[1:len(lista_pelicula)])
    anio = valores['year'].to_string().split()[1]
    popularidad = valores['popularity'].to_string().split()[1]

    return f"La pelicula {pelicula} fue estrenada en el año {anio} con un score/popularidad de {popularidad}."


@app.get("/Votos Titulo")
def votos_titulo(titulo_filmacion: str):
    for i in data_movies['title']:
        if i == titulo_filmacion:
            valores = data_movies[data_movies['title'] == i]
            break

    lista_pelicula = valores['title'].to_string().split()
    pelicula = ' '.join(lista_pelicula[1:len(lista_pelicula)])
    anio = valores['year'].to_string().split()[1]
    cantidad_votos = float(valores['vote_count'].to_string().split()[1])
    promedio_votos = valores['vote_average'].to_string().split()[1]

    if cantidad_votos < 2000:
        return f"La pelicula {pelicula} no tiene la cantidad suficiente de votos para sacar el promedio."
    else:
        return f"La pelicula {pelicula} fue estrenada en el año {anio}. La misma cuenta con un total de {cantidad_votos} valoraciones, con un promedio de {promedio_votos}."
    

@app.get("/Actores")
def get_actor(actor: str):
    cantidad_peliculas = 0
    id_peliculas = []
    #retornos = []
    suma_retornos = 0

    for i in range(len(data_credits)):
        if actor in data_credits['actores'][i]:
            id_peliculas.append(data_credits['id'][i])
            cantidad_peliculas += 1

    for i in id_peliculas:
        valores = data_movies[data_movies['id'] == i]
        #retornos.append(float(valores['return']))
        suma_retornos += float(valores['return'])

    return (f"El actor {actor} ha participado en {cantidad_peliculas} peliculas, el mismo ha conseguido un retorno de {round(suma_retornos, 2)} con un promedio de {round(suma_retornos/cantidad_peliculas, 2)}.")

@app.get("/Directores")
def get_director(director: str):
    id_peliculas = []
    #retornos = []
    suma_retornos = 0
    peliculas = []
    oracion = ""

    for i in range(len(data_credits)):
        if director in data_credits['directores'][i]:
            id_peliculas.append(data_credits['id'][i])

    for i in id_peliculas:
        valores = data_movies[data_movies['id'] == i]
        #retornos.append(float(valores['return']))
        suma_retornos += float(valores['return'])
        pelicula = [valores['title'].to_list(), valores['release_date'].to_list(), valores['budget'].to_list(), valores['revenue'].to_list(), valores['return'].to_list()]
        peliculas.append(pelicula)

    oracion = f"El director {director} ha conseguido un retorno de {round(suma_retornos,2)} y ha dirigido las siguientes peliculas: "
    salida = oracion
    oracion = ""

    for i in range(len(peliculas)):
        oracion = f"Titulo: {peliculas[i][0][0]}, Fecha de estreno: {peliculas[i][1][0]}, Presupuesto: {peliculas[i][2][0]}, Ingresos: {peliculas[i][3][0]}, Retorno: {peliculas[i][4][0]}. "
        salida += oracion

    return salida