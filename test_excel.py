import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://blog.gofreight.co/"
web = requests.get(URL)
target = BeautifulSoup(web.text, "html.parser")

Title = BeautifulSoup.find_all("a", {"class": "title"})
A = []
i = list(range(0,20))
for index in i:
    result = Title[index]
    A.append(result)
    print(A)




""" 
web = []
for i in contents:
    if "https" in str(i['href']):
            web.append(str(i['href']))
print(web)

df = {'Page title':[], 'URL Link':[]}
for index in A:
    index = index.split("\n")[0]
    df['Page title'].append(index)
for url in web:
    url = url.split("\n")[0]
    df['URL Link'].append(url)

# df = pd.DataFrame.from_dict(df, orient = 'index') # 橫的
df = pd.DataFrame.from_dict(df) # 直的
df.to_csv("file.csv", index = False) # 也可以將csv改成xlsx """