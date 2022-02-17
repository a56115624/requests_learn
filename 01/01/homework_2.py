from base64 import encode
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

# wb = Workbook()
# ws = wb.active
# title = ["幣別","現金匯率.本行買入","現金匯率.本行賣出","即期匯率.本行買入", "即期匯率.本行賣出"]
# ws.append(title)
#取得台灣銀行牌告匯率網站
r1 = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
soup = BeautifulSoup(r1.text,'html.parser')
for i in soup.find_all("tr"):
    r2 = i.find("div",{"class":"hidden-phone print_show"}).text
    print(r2)
# for i in soup.find_all("tr"):
#     print(i.find("div",{"class":"hidden-phone print_show"}).text)
    # print(i.find("td",{"class":"rate-content-cash text-right print_hide"}))
    # print(i.find("td",{"class":"rate-content-sight text-right print_hide hidden-phone"}))
    
# for i in soup.find_all("tr"):
#     recipe = []
#     recipe.append(i.find("div",{"class":"visible-phone print_hide"}))
#     recipe.append(i.find("td",{"class":"rate-content-cash text-right print_hide"}))
#     recipe.append(i.find("td",{"class":"rate-content-sight text-right print_hide hidden-phone"}))



