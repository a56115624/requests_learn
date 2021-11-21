import requests as req
from openpyxl import Workbook


wb = Workbook()
ws = wb.active

title = ['菜名','介紹','食材']
ws.append(title)


for a in range(15):
    home = r'https://icook.tw'
    target = input('請輸入你要查詢的食材')
    url = f'{home}/search/{target}'
    ret = req.get(url,
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"})

   

    root_json = ret.json()
    
    for data in root_json['li']:
        course = []
        course.append(data['class']['browse-recipe-item']['h2'])
        course.append(data['class']['browse-recipe-item']['blockquote'])
        course.append(data['class']['browse-recipe-item']['p'])

        ws.append(course)

wb.save('data.xlsx')

