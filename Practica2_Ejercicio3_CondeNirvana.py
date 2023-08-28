#Conde Lopez Nirvana Desiree Ejercicio 3
import pandas as pd

def resumen_estadisticas(df):
    estadisticas = {
        "Mínimo": df.min(),
        "Máximo": df.max(),
        "Media": df.mean()
    }
    df_stats = pd.DataFrame(estadisticas)
    return df_stats

def cotizaciones(path):
    df_cotizacion = pd.read_csv(path, sep=";", decimal=",")
    columnas_numericas = df_cotizacion.select_dtypes(include=[float, int]).columns
    df_estadisticas = resumen_estadisticas(df_cotizacion[columnas_numericas])

    return df_estadisticas

path_cotizacion = "https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv"

df_resultado = cotizaciones(path_cotizacion)
print(df_resultado)
