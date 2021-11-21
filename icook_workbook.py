import requests as req
from openpyxl import Workbook


wb = Workbook()
ws = wb.active

title = ['菜名','介紹','食材']
ws.append(title)

header = {
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'cookie': 'visitor=13728257989256429706; _pbjs_userid_consent_data=3524755945110770; _gcl_au=1.1.1407276380.1636535883; __auc=1644db7717d0923d5aa8c8a7763; _cc_id=17d75d4dc0c20fd4d2f4d9c602b0a854; dable_uid=64813915.1557747589578; _fbp=fb.1.1636536101280.619772029; truvid_protected={"val":"c","level":2,"geo":"TW","timestamp":1636775067}; most_ga=GA1.2.34690171.1636535883; one_fp=%252213fd4b6d679c436ade61d611fd0d848d%2522; oid=%257B%2522oid%2522%253A%25229b7d9231-7202-11e9-9754-0242ac120003%2522%252C%2522ts%2522%253A1557369113%252C%2522v%2522%253A%252220201117%2522%257D; CF-IPCountry=TW; panoramaId_expiry=1638066209071; panoramaId=d4bfea3c0a866129f65ae762024b16d53938b168a3f135f885f5223c5287044e; __gads=ID=96c2766af3d6a92e:T=1636535884:S=ALNI_MYS5el3OR4U5OJhhi0U7TkmdS4oww; __asc=70e82b0f17d404e47b5d08ba46b; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.2029110792.1637461412; _dc_gtm_UA-18942613-4=1; _gat_UA-18942613-4=1; CSRF-TOKEN=kkzUbp1Tx6Fmvzp4duAAULcV5bN6bsq%2BpyGenv9b0f9pn5dWTQzorbfmitF7C2p8KZqq8EWfGXIE%2B62hVNsqOg%3D%3D; _icook_sess=SFphMHdGa0MwKzk2V3VZc3ZmVmoxcjk1aGJxV1laTS9DdFRWVTFzb1V3bDRUaEJ0Z2NVRjF0Z3NTNjBCTXpUd2FBY2xZVjlVVlVML3JZV1lmekw3S0czeWk5eTl3bm9SZk96VzVjbCtIWGFJVlp1MkQ1VDVtMStHdVFGblNhV1NmSVd5S1RENGdweXZuSWRWZ1hmN2p5UlY3ZjZtd3ExMlAyT0ttY09vRjkydFFiamt1RTZIdW53ZHUvbEV0aHdlNjh2czFoLy83M1RHS3FNOU5wVHN1dlREVFdvNjZhYnljMEpQSVRJK091ZTVNT3hDUStvei9kNjJPR3V0Sjh5Yy0tOVAzTFpoQjBaaGlRS1hsY3JtMzJDUT09--226e7665715ef545bd928e815b4d37de0a13cccf; _ga_Q65WJCEHK3=GS1.1.1637461409.21.1.1637461417.52; _ga_ZKZX6M179R=GS1.1.1637461410.21.1.1637461418.52; _ga=GA1.2.34690171.1636535883; sent-cid=1637461433'
}

search = input("請輸入要查詢的關鍵字")
url = "https://icook.tw/search/"
url = url + str(search)
#print(url)
r = req.get(url, headers=header)
print(r)

""" root = r.text()
    

course = []
course.append(['h2']['class']['browse-recipe-name'])
course.append(['blockquote']['class']['browse-recipe-content-description'])
course.append(['p']['class']['browse-recipe-content-ingredient'])

ws.append(course)

wb.save('data.xlsx') """
