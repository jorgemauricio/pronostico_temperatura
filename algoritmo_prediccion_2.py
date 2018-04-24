#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#######################################
# Author: Jorge Mauricio
# Email: jorge.ernesto.mauricio@gmail.com
# Date: 2018-02-01
# Version: 1.0
#######################################
"""

# librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression as LinReg


def main():

    # leer csv
    df = pd.read_csv("resultados/compilado_mexico_temp_R.csv")

    df.sort_values(by="Año", inplace=True)

    # lons and lats
    lons = np.array(df["Long"])
    lats = np.array(df["Lat"])

    # ciclo para la generación de la predicción
    contador = 0

    # dataframe
    new_df = pd.DataFrame(columns="Long Lat Año Ene Feb Mar Abr May Jun Jul Ago Sept Oct Nov Dic".split())
    for lon, lat in zip(lons, lats):
        # df temporal
        df_temporal = df.loc[(df["Long"] == lon) & (df["Lat"] == lat)]

        # ordenar valores por año
        grouped = df_temporal.groupby("Año").mean()

        # valores x y y
        X = grouped.index.values.reshape(-1, 1)
        y_Ene = grouped["Ene"].values
        y_Feb = grouped["Feb"].values
        y_Mar = grouped["Mar"].values
        y_Abr = grouped["Abr"].values
        y_May = grouped["May"].values
        y_Jun = grouped["Jun"].values
        y_Jul = grouped["Jul"].values
        y_Ago = grouped["Ago"].values
        y_Sept = grouped["Sept"].values
        y_Oct = grouped["Oct"].values
        y_Nov = grouped["Nov"].values
        y_Dic = grouped["Dic"].values

        # declarar la regresión
        reg_1 = LinReg()
        reg_2 = LinReg()
        reg_3 = LinReg()
        reg_4 = LinReg()
        reg_5 = LinReg()
        reg_6 = LinReg()
        reg_7 = LinReg()
        reg_8 = LinReg()
        reg_9 = LinReg()
        reg_10 = LinReg()
        reg_11 = LinReg()
        reg_12 = LinReg()

        # ajustar el modelo
        reg_1.fit(X,y_Ene)
        reg_2.fit(X,y_Feb)
        reg_3.fit(X,y_Mar)
        reg_4.fit(X,y_Abr)
        reg_5.fit(X,y_May)
        reg_6.fit(X,y_Jun)
        reg_7.fit(X,y_Jul)
        reg_8.fit(X,y_Ago)
        reg_9.fit(X,y_Sept)
        reg_10.fit(X,y_Oct)
        reg_11.fit(X,y_Nov)
        reg_12.fit(X,y_Dic)

        ene = []
        feb = []
        mar = []
        abr = []
        may = []
        jun = []
        jul = []
        ago = []
        sept = []
        octu = []
        nov = []
        dic = []
        new_longs = []
        new_lats = []
        anios = []

        # predicción
        i = 2018
        print("Long: {} Lat: {} Pred: {}".format(lon, lat, i))
        ene.append(reg_1.predict(i))
        feb.append(reg_2.predict(i))
        mar.append(reg_3.predict(i))
        abr.append(reg_4.predict(i))
        may.append(reg_5.predict(i))
        jun.append(reg_6.predict(i))
        jul.append(reg_7.predict(i))
        ago.append(reg_8.predict(i))
        sept.append(reg_9.predict(i))
        octu.append(reg_10.predict(i))
        nov.append(reg_11.predict(i))
        new_lats.append(lat)
        new_longs.append(lon)
        anios.append(i)

        contador += 1
        print(contador)

        d = {"Long":np.array(new_longs),
             "Lat": np.array(new_lats),
             "Año": np.array(anios),
             "Ene": np.array(ene),
             "Feb": np.array(feb),
             "Mar": np.array(mar),
             "Abr": np.array(abr),
             "May": np.array(may),
             "Jun": np.array(jun),
             "Jul": np.array(jul),
             "Ago": np.array(ago),
             "Sept": np.array(sept),
             "Oct": np.array(octu),
             "Nov": np.array(nov),
             "Dic": np.array(dic)}


        new_df = new_df.append(d, ignore_index=True)
    new_df.to_csv("resultados/predicciones_temp.csv")

if __name__ == '__main__':
    main()
