import requests
import pandas as pd
from bs4 import BeautifulSoup

response=requests.get("https://realpython.github.io/fake-jobs/")
print(requests.status_code)
print(response.content)