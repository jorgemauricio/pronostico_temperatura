import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():

    # path folder proyecto
    path_folder = "/home/jorge/Documents/Research/pronostico_temperatura/"
    # path folder archivos
    path_archivos = "/home/jorge/Documents/Research/pronostico_temperatura/data"
    # lista de archivos de tempratura
    lista_de_archivos = [x for x in os.listdir(path_archivos) if x.endswith('')]

    # DataFrame
    data = pd.DataFrame(columns="Long Lat Año Mes Valor".split())

    cols = ["Long","Lat","Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sept","Oct","Nov","Dic"]

    # estructura DataFrame
    for archivo in lista_de_archivos:

        titulo, anio = archivo.split(".")

        path_archivo = "{}/{}".format(path_archivos, archivo)

        df_temp = pd.read_table(path_archivo, sep="\s+", header=None)

        df_temp.columns = cols

        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sept","Oct","Nov","Dic"]

        for index, row in df_temp.iterrows():
            for mes in meses:
                df = {"Long": row["Long"],
                        "Lat": row["Lat"],
                        "Año": anio,
                        "Mes": mes,
                        "Valor": row[mes]}
            data = data.append(df, ignore_index=True)
        print("*****", archivo)

    data.to_csv("compilado2.csv")

if __name__ == '__main__':
    main()
