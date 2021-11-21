import requests
from bs4 import BeautifulSoup

home = r'https://icook.tw'
target = input('請輸入你要查詢的食材')
for i in range(15):
  url = f'{home}/search/{target}'
  url = url + str(i)
  print(url)
  ret = requests.get(url,
  headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})
  print(ret)



  b1=BeautifulSoup(ret.text,"html.parser")
  for b2 in b1.find_all("li",{"class":"browse-recipe-item"}):
    print(b2.find("h2").text) 
    print(b2.find("blockquote").text) 
    print(b2.find("p").text) 
    
