# Individual_Henry_Project1

## Descripción del proyecto a realizar
* Este proyecto es un proyecto individual en el que se requeria realizar un MVP (Minimo Producto Viable), sobre dos datasets de peliculas. El proyecto tenia unos requisitos obligatorios dentro de los cuales estaban hacer ciertas transformaciones, el desarrollo de una API con 7 funciones, hacer el deployment para que este quede de manera publica, un sistema de recomendación y un video de entre 6 y 9 minutos explicando lo que se realizo.

* El siguiente enlace es el enlace del repo donde se dio toda la información: https://github.com/soyHenry/fe-ct-pimlops2?tab=readme-ov-file

## Paso a paso

### 1. Revisión de los datos
* Lo primero que se hizo fue revisar los diccionarios que se entregaron en el repositorio, y después se revisaron los datos en excel, no sirve de mucho ya que son muchos datos y excel no permite pasarlos de texto a columnas.
* Después se revisaron los datos dentro de python.

### 2. Creación del repositorio, instalación de librerias y creación de entorno virtual
* Primero se creo el repositorio en el GitHub, se clono en una carpeta dentro del sistema local, después se creo un entorno virtual de python con la versión 3.10.11. Se eligio esta versión porque fue la ultima que se encontro para la versión 3.10, además se escogio la 3.10 porque se requeria una versión estable para las librerias y que funcione correctamente con la FASTAPI. Al final se instalaron las librerias, durante todo el proyecto se han ido instalando librerias.

### 3. Transformaciones y primer proceso de ETL.
* Se realizaron todas las trandformaciones obligatorias y se realizaron algunas transformaciones que se consideraban oportunas, para después trandformar el dataframe y pasarlo a formato a formato csv, de esta manera se puede llamar en el archivo main.py y utilizarlo sin problemas.

### 4. Funciones
* Se realizaron las 6 funciones obligatorias en un cuaderno de jupyter de pruebas y después se pasaron al archivo main.py.

### 5. Creación de la API en local
* Después de finalizar las 6 funciones se decidio llevar las funciones a una API ejecutada desde el mismo sistema (local) para revidar como funcionaba la librería de FASTAPI y ver si las funciones estaban funcionando de manera correcta.

### 6. Primer despliegue en Render
* Despues de revisar que todo funcionaba correctamente de manera local, se decidio llevar el progreso a render, en el cual se tuvo que especificar la versión de Python que se utilizo, un archivo de requirements que tueviera todas las librerías y las versiones que se utilizo por cada uno y se tuvo que comentar la librería pywin32 ya que arrojaba error cuando Render intentaba construir.

### 7. EDA
* Después de revisar que las funciones se ejecutaban y arrojaban una respuesta de manera correcta, se decicio hacer el analisis exploratorio de datos (EDA), donde se revisaron los datos. Se reviso si habían valores nulos, si existian outliers en las columnas que tuvieran tipos de datos enteros o de punto flotante, se realizo el análisis de correlación entre las variables, y al final se hicieron 3 nubes de palabras para ver las palabras más repetidas entre ciertas columnas del dataset.

### 8. Segundo ETL
* En este seguno ETL se busco reducir el tamaño del dataset original a lo menor posible para poder ser utilizado en el modelo de recomendación. Al final se decidio que el dataset resultante solo tendría las columnas de titulo, id, overview, tagline y generos. Esto con el fin de buscar la mejor similitud entre las peliculas.

### 9. Modelo de recomendación
* Se decidio utilizar el modelo que nos recomendaron desde un inicio, el modelo de la similitud del coseno. Para utilizar este modelo se tuvo que concatenar el titulo, el overview y el tagline por cada registro de pelicula, para depues remover las palabras que no tienen una gran relevancia en el texto y así al final concatenar estas palabras resultantes y poder utilizar un vectorizador para vectorizar cada concatenación con respecto a las demás peliculas.
* Cuando esto ya esta hecho queda una matriz la cual se le pasa al modelo de similitud del coseno y este realiza su proceso para poder decidir si una pelicula es o no similar a otra. La similitud del coseno también arroja una matriz de valores entre 1 y 0, si algún valor esta cerca a 1 eso quiere decir que ese registro es muy similar al que se esta evaluando, en cambio si es cero significa que no son similares.
* Como el dataset es muy grande se tuvo que reducir su tamaño para que sirviera al momento de desplegarlo en la herramienta Render.

### 10 Segundo despliegue en Render
* Despues de revisar que el modelo de recomendación funcionara correctamente se decidio llevar a Render. En este paso se tuvo que reducir 3 vo 4 veces el dataset que iba a ser utilizado en Render ya que consumia mucha memoria y no permitia su despliegue. Al final se dejo el dataset con los primeros 5000 registros y Render pudo desplegar.
