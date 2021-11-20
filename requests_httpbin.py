#TOOD:https://httpbin.org/#/ 這是一個可以模擬各種網站的東西


import requests as req
#get
""" url = req.get("https://httpbin.org/get",
params={
    'page':'2',
    'count':'5'
})
print(url.text) """
#post
""" url = "https://httpbin.org/post"
params={
    'page':'2',
    'count':'5'
}
data={
    'name':'shane',
    'age':'29'
}

u = req.post(url, params=params, json=data)

print(u.text) """
#將照片讀取後上傳到網站上
""" url = "https://httpbin.org/post"
params={
    'page':'2',
    'count':'5'
}
data={
    'name':'shane',
    'age':'29'
}

with open('123.jpg',mode ='rb')  as file:
    imge = {'upload_image' : file.read() }
r = req.post(url, params=params, data=imge)
print(r.text)
 """
#改變User-Agent讓自己看起來像瀏覽器
""" url = "https://httpbin.org/post"
params={
    'page':'2',
    'count':'5'
}
data={
    'name':'shane',
    'age':'29'
}
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
r = req.post(url, params=params, headers=header)
print(r.text)
 """
#模擬一個需要登陸的網站
""" url = "https://httpbin.org/basic-auth/123/456"
params={
    'page':'2',
    'count':'5'
}
data={
    'name':'shane',
    'age':'29'
}
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

r = req.get(url,auth=('123','456'))
print(r.text) """
#模擬一個網站要登陸很久的情況
url = "https://httpbin.org//delay/{3}"
params={
    'page':'2',
    'count':'5'
}
data={
    'name':'shane',
    'age':'29'
}
header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

r = req.get(url,timeout=5)
print(r)