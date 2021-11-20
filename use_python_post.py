#用python在匹克幫發文
import requests as req

url = "https://qa.pixnet.cc/personal_articles?with_member_profile=true"

headers ={
    "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkucGl4bmV0LmNjIiwibWVtYmVyX3VuaXFpZCI6IjUzMDA1NjE5OGE4M2M5MWIyMSIsInRva2VuIjoiYWUzMzI0ZWJhNjI1MTQ0YWRjZWMxMmVhOTJmZjVkYjciLCJpYXQiOjE2MzczOTQ1MDcsImV4cCI6MTYzNzM5ODEwN30.i5vrfNuq06aVCNL5s5F1zFPqPIO46Sy7fwglgACiumw",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"

}

data = '{"content":"456897","source":"www","pictures":[]}'

r = req.post(url, headers=headers, data=data)
print(r)