import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By#
from webdriver_manager.chrome import ChromeDriverManager


s=Service(ChromeDriverManager().install())
opc=Options()

opc.add_argument("--window-size=1020,1200")
navegador=webdriver.Chrome(service=s,options=opc)
navegador.get("https://es-la.facebook.com/")


txtEmail=navegador.find_element(By.NAME,"email")
print(txtEmail)
txtEmail.send_keys("usuario@gmail.com")
time.sleep(7)
txtPass=navegador.find_element(By.NAME,"pass")
print(txtPass)
txtPass.send_keys("123")
time.sleep(4)

navegador.save_screenshot("img_test.png")
btnLogin=navegador.find_element(By.NAME,"login")
btnLogin.click()


print(navegador.title)
time.sleep(5)