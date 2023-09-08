import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Configuración del navegador
s = Service(ChromeDriverManager().install())
opc = Options()
opc.add_argument("--window-size=1020,1200")
navegador = webdriver.Chrome(service=s, options=opc)

navegador.get("https://www.amazon.com/")

search_box = navegador.find_element(By.ID, "twotabsearchtextbox")
search_term = "python"
search_box.send_keys(search_term)
search_box.submit()


time.sleep(10)

Soup = BeautifulSoup(navegador.page_source, "html.parser")
search_results = Soup.find_all("div", class_="s-result-item")

resultados = []

for result in search_results:
    title = result.find("h2")
    if title:
        titulo = title.text.strip()
    else:
        titulo = "No se encontró título"

    price = result.find("span", class_="a-price")
    if price:
        precio = price.find("span", class_="a-offscreen").text.strip()
    else:
        precio = "Precio no disponible"

    link = result.find("a", class_="a-link-normal")
    if link:
        enlace = "https://www.amazon.com" + link.get("href")
    else:
        enlace = "Enlace no disponible"

    # Agregar los datos a la lista de resultados
    resultados.append({"Título": titulo, "Precio": precio, "Enlace": enlace})

# Cerrar el navegador
navegador.close()

# Crear un DataFrame con los resultados y guardar en un archivo CSV
data_frame = pd.DataFrame(resultados)
data_frame.to_csv("resultados_amazon.csv", index=False)
