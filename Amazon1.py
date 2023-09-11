#####Nirvana Desiree Conde Lopez
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
search_term = input("Ingrese el término de búsqueda: ")
num_paginas = int(input("Ingrese el número de páginas a buscar en Amazon: "))

search_box = navegador.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys(search_term)
search_box.submit()

time.sleep(10)

navegador.save_screenshot("img_amazon.png")