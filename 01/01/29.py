import requests
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

url = "https://rate.bot.com.tw/xrt?Lang=zh-TW"

r1 = requests.get(url)
soup = BeautifulSoup(r1.text,'html.parser')
print(soup)
for i in soup.find('div',{'class':"hidden-phone print_show"}).text:
    print(i)
