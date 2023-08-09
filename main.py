#Importamos los modulos que usaremos
import pandas as pd
import os
import glob
from sqlalchemy import create_engine
#Obtenemos todos los archivos CSV que estan en el mismo folder que el programa
archivos = glob.glob('*.csv')
#Por cada archivo en los archivos CSV
for file in archivos:

    #Convertimos el CSV en un DataFrame de pandas
    df = pd.read_csv(file)

    user = "postgres" # Usario del engine
    password = "admin" # Contraseña 
    host = "localhost" # HOST
    port = "5432" # Puerto
    database = "proyecto1" # Nombre de la base de datos

    #Creamos la conexion con nuestro engine
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    #Convertimos el DataFrame en una tabla SQL
    df.to_sql(file.replace('.csv',''), engine)
