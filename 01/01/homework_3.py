
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active
title = ["幣別","現金匯率.本行買入","現金匯率.本行賣出","即期匯率.本行買入", "即期匯率.本行賣出"]
ws.append(title)
r1 = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
soup = BeautifulSoup(r1.text,'html.parser')
data = soup.find("table",{"class":"table table-striped table-bordered table-condensed table-hover"})
# print(data)
coin = data.find_all("div",{"class":"hidden-phone print_show"})
# print(coin[1].text.strip())
cash_exchange_rate = data.find_all("td",{"class":"rate-content-cash text-right print_hide"})
# print(cash_exchange_rate[0].text.strip())
now_exchange_rate = data.find_all("td",{"class":"rate-content-sight text-right print_hide"})
#print(now_exchange_rate[0].text.strip())
# print("幣別\t\t現金匯率.本行買入\t現金匯率.本行賣出\t即期匯率.本行買入\t即期匯率.本行賣出")
for n in range(0,len(coin)):
    # print(coin[n].text.strip()+"\t"+cash_exchange_rate[n*2].text+"\t"+cash_exchange_rate[n*2+1].text+"\t"+now_exchange_rate[n*2].text+"\t"+now_exchange_rate[n*2+1].text)
    put = []
    put.append(coin[n].text.strip())
    put.append(cash_exchange_rate[n*2].text)
    put.append(cash_exchange_rate[n*2+1].text)
    put.append(now_exchange_rate[n*2].text)
    put.append(now_exchange_rate[n*2+1].text)
    ws.append(put)
wb.save("homework_shane.xlsx")







