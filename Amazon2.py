#####Nirvana Desiree Conde Lopez
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size=1020,1200")
navegador = webdriver.Chrome(service=s, options=opc)

navegador.get("https://www.amazon.com/")
search_term = input("Ingrese el término de búsqueda: ")
num_paginas = int(input("Ingrese el número de páginas a buscar en Amazon: "))

search_box = navegador.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_term)
search_box.submit()

time.sleep(10)

navegador.save_screenshot("img_amazon.png")
resultados = {"Título": [], "Precio": [], "Calificación": [], "Fecha de Entrega": []}

for pagina in range(1, num_paginas + 1):
    Soup = BeautifulSoup(navegador.page_source, "html.parser")
    search_results = Soup.find_all("div", attrs={"class":"s-result-item"})
    navegador.save_screenshot("img_amazon.png")
    #######en el primer resultado sale anuncios o promociones
    for i in range(1,len(search_results)):
        result=search_results[i]

        title = result.find("h2")
        if title:
            titulo = title.text.strip()
        else:
            titulo = "No se encontró título"

        price = result.find("span", attrs={"class":"a-price"})
        if price:
            precio = price.find("span", attrs={"class":"a-offscreen"}).text.strip()
        else:
            precio = "Precio no disponible"

        rating = result.find("span", attrs={"class":"a-icon-alt"})
        if rating:
            calificacion = rating.text.strip()
        else:
            calificacion = "No disponible"

        delivery = result.find("div", attrs={"class":"a-row s-align-children-center"})
        if delivery:
            fecha_entrega = delivery.text.strip()
        else:
            fecha_entrega = "No disponible"

        resultados["Título"].append(titulo)
        resultados["Precio"].append(precio)
        resultados["Calificación"].append(calificacion)
        resultados["Fecha de Entrega"].append(fecha_entrega)


navegador.close()

data_frame = pd.DataFrame(resultados)
data_frame.to_csv("resultados_amazon.csv")
