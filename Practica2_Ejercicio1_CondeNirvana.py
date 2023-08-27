#NirvanaDesireeConde Lopez Practica2 Ejercicio1
import pandas as pd


DataFrameVentas={"Mes":["Enero","Febrero","Marzo","Abril"],
                 "Ventas":[30500,35600,28300,33900],
                 "Gatos":[22000,23400,18100,20700]
                 }

df_ventas=pd.DataFrame(DataFrameVentas)
print(df_ventas)

def Balance(df,meses):
    df_filtrado = df[df["Mes"].isin(meses)]
    balance_total = df_filtrado["Ventas"].sum() - df_filtrado["Gatos"].sum()
    return balance_total


df_ventas = pd.DataFrame(DataFrameVentas)
meses_a_considerar = ["Enero", "Marzo"]
balance_resultado = Balance(df_ventas, meses_a_considerar)
print("Balance total:", balance_resultado)


