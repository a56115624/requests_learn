import requests
from bs4 import BeautifulSoup
import csv

filename = 'ssss'
home = r'https://icook.tw'
target = input('請輸入你要查詢的食材')
tmp = []
for i in range(15):
    url = f'{home}/search/{target}'
    url = url + str(i)
    # print(url)
    ret = requests.get(url,
                       headers={
                           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})
    # print(ret)
    b1 = BeautifulSoup(ret.text, "html.parser")

    for b2 in b1.find_all("li", {"class": "browse-recipe-item"}):

        tmp.append(
            {
                '菜名' :b2.find("h2").text.strip(),
                '網址' :home + b2.find("a").attrs["href"] ,
                '食材' :b2.find("p").text.strip(),
            }
            )
        # print("菜名:" + b2.find("h2").text)
        # print("網址:" + b2.find("a").attrs["href"])
        # print("食材:" + b2.find("p").text)



with open(filename + '.csv', 'w', newline='',encoding='utf-8') as csvfile:
    # 定義欄位
    fieldnames = ['菜名', '網址', '食材']

    # 將 dictionary 寫入 CSV 檔
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # 寫入第一列的欄位名稱
    writer.writeheader()

    # 寫入資料
    for qa in tmp:
        writer.writerow(qa)