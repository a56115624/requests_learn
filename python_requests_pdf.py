#下載pdf
import requests as req

url = req.get("https://www.lib.ntu.edu.tw/doc/cl/etdsguide.pdf")#讀取影片要用content

with open('123.pdf',mode ='wb')  as file:
    file.write(url.content)
