#爬取網站
import pandas as pd
url="https://rate.bot.com.tw/xrt?Lang=zh-TW"
r1 = pd.read_html(url)
#獲得表格
r2 = r1[0]
#檢視表格
r2.head()
#檢視欄位
r2.columns
#全部的row(行)以及0:5的index(列)
r3=r2.iloc[:,:5]
r3.head()
#自訂欄位名稱
r3.columns=[u"幣別",u"現金匯率-本行買入",u"現金匯率-本行賣出",u"即期匯率-本行買入",u"即期匯率-本行賣出"]
r3.head()
# print(currency)
r3.to_excel("homework.xlsx")