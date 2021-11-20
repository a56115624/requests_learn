#下載圖片
import requests as req

url = req.get("https://tpc.googlesyndication.com/simgad/9154225785623672266?")#讀取影片要用content

with open('123.jpg',mode ='wb')  as file:
    file.write(url.content)
