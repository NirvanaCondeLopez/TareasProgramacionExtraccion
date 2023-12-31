import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://realpython.github.io/fake-jobs/")
print(response.status_code)
#print(response.content)


if response.status_code==200:
    soup=BeautifulSoup(response.content,"html.parser")###contenido es de tipo html y se ocupa descomponer
    lista_divs=soup.find_all("div",attrs={"class":"card-content"})
    data={"puesto":[],"empresa":[],"ciudad":[],"fecha":[]}

    for div in lista_divs:
        puesto=div.find("h2",attrs={"class":"title is-5"})
        company=div.find("h3",attrs={"class":"subtitle is-6 company"})
        city=div.find("p",attrs={"class":"location"})
        date=div.find("time")
        "".strip()
        data["puesto"].append(puesto.text)
        data["empresa"].append(company.text)
        data["ciudad"].append(city.text.strip)
        data["fecha"].append(date.text)

        print(lista_divs[0].prettify())
        print("\n")

    data_df=pd.DataFrame(data)
    data_df.to_csv("Datasets/fake_jobs.csv")
    ###print(soup.head.title)
else:
    print(f"ERROR {response.status_code}AL MOMENTO DE CARGAR LA PAGINA")

