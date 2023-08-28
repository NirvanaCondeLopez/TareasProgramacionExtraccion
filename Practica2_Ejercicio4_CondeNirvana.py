#Conde Lopez Nirvana Desiree Ejercicio 4
import pandas as pd

path="https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv"
df=pd.read_csv(path,sep=",")
print(df)
def Dimensiones():
    print("Filas:", df.shape[0])
    print("Columnas:", df.shape[1])

def NumeroDatos():
    print("\nNúmero de datos y nombres de las columnas:")
    print("Número de datos:", df.size)
    print("Nombres de columnas:", df.columns.tolist())

def PrimerasyUltimas():
    print("\nPrimeras 10 filas:")
    print(df.head(10))
    print("\nÚltimas 10 filas:")
    print(df.tail(10))

def Porcentajes_Sobrevivientes_Muertes():
    total=df.shape[0]
    sobrevivientes=df["Survived"].sum()
    muertes=total-sobrevivientes
    Porcentaje_sobre=(sobrevivientes/total)*100
    Porcentaje_muertes=(muertes/total)*100

    print("Porcentaje sobrevivientes:",Porcentaje_sobre)
    print("Porcentaje muertes:",Porcentaje_muertes)

def Porcentaje_Sobrevivientes_Clase():
    Porce_muertes_clase=df.groupby("Pclass")["Survived"].mean() *100
    print("\nPorcentaje de personas que sobrevivieron en cada clase:")
    print(Porce_muertes_clase)




Dimensiones()
NumeroDatos()
PrimerasyUltimas()
Porcentajes_Sobrevivientes_Muertes()
Porcentaje_Sobrevivientes_Clase()