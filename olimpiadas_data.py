import time
import pandas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By#
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup



s=Service(ChromeDriverManager().install())
opc=Options()

opc.add_argument("--window-size=1020,1200")
navegador=webdriver.Chrome(service=s,options=opc)
navegador.get("http://www.olympedia.org/statistics/medal/country")

cmdYear=navegador.find_element(By.NAME,"edition_id")
cmdGender=navegador.find_element(By.NAME,"athlete_gender")

GenderOption=cmdGender.find_elements(By.TAG_NAME,"option")
##print(GenderOption[0].text)
##print(GenderOption[1].text)
##print(GenderOption[2].text)
Option_groupsss=cmdYear.find_elements(By.TAG_NAME,"optgroup")

listaA=Option_groupsss[0].find_elements(By.TAG_NAME,"option")

datos={
    "country":[],
    "year":[],
    "gender":[],
    "gold":[],
    "silver":[],
    "bronze":[],
    "total":[]
}

for gender in GenderOption[1:]:
    gender.click()

    for year in listaA:
        year.click()
        time.sleep(3)
        Soup=BeautifulSoup(navegador.page_source,"html.parser")
        table = Soup.find("table", attrs={"class": "table table-striped"})
        list_rows=table.find_all("tr")

        for row in list_rows[1:]:
            datos["gender"].append(gender.text)
            datos["year"].append(year.text)
            values=row.find_all("td")
            datos["country"].append(values[0].text)
            datos["gold"].append(values[2].text)
            datos["silver"].append(values[3].text)
            datos["bronze"].append(values[4].text)
            datos["total"].append(values[5].text)

navegador.close()


data_f=pd.DataFrame(datos)
data_f.to_csv("data_olimpiadas.csv")






