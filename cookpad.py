import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook

ingredient = input("請輸入你需要的食材:")
r1 = requests.get(f'https://cookpad.com/tw/%E6%90%9C%E5%B0%8B/{ingredient}?event=search.typed_query',
        headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'cookie':'ab_session=0.22805529257603352; f_unique_id=6efac12f-8eab-4f3d-acf3-a23a1f8f1d91; _pxhd=TovEuEN-xfV7Ar0YHtuH3Qr-sTTLjOPog6ablRteoLQ7ZIj06a6KEefxj/2ztcbi9m68-CCc29bxWOWlA0Fx9g==:/csEACcDK0GMfB/75dfhxJ11vmXScRu1SgEvSGuHYrD6uCIMOlbYdtmcm4UJmp8yP0f8iRvo5hlNvgfvPbyucF13t6nhL2QIjpMaG-RJh9649tJmImHzvdWfudqfPsGXap86XcjcWqIyeQ4BHreaeg==; _ga=GA1.2.2007734559.1640229926; _gid=GA1.2.1789152356.1640229926; pxcts=f93458b0-639f-11ec-949e-19083dd0c3d0; _pxvid=f7e01d6a-639f-11ec-85d3-447563516857; keyword_history_zh-TW=%5B%22%E7%89%9B%E8%82%89%22%5D; accept_cookies_and_privacy_and_terms=1; recipe_view_count_zh-TW=1; _global_web_session=o%2BvjLGo9kq769UhZik7iIFo6in%2F8HXTz%2Fd60sMvuaXYPErahI3Vj8Uo32UPPh4uiCVD2KYJGTUUQffLoB8OX88suAaPki0PgYFnSavzjZGu2wpTZUb80So2wUVCrhZW8kBp5oUbLynTkHDW8UFYrR3uX2PRA781WMGsVoaYK4LGZtiHGnOQeSMg4WsPpOT56kAOzf95YPeX6BE4oV%2FCuEiMm11lgs9oGlg1hXrOFYPE2fwqmohthK7l8yYQC8zTmCqCKsqjzY2Mv63T76mPeAaGIhXNKPfhP4mZI6wNjxapR%2FastdoayXbSXNGIywnOFU1Myg75FgwLy3bESTxeJ--zY0cxzTt2vhOeqMk--qmYD2%2BrCkbL32%2Fg5F6Fqhw%3D%3D; _px2=eyJ1IjoiZjgxZDZhNzAtNjM5Zi0xMWVjLTlkMjgtYjcwMGE1M2ZkODc5IiwidiI6ImY3ZTAxZDZhLTYzOWYtMTFlYy04NWQzLTQ0NzU2MzUxNjg1NyIsInQiOjE2NDAyMzA0NjkxNzcsImgiOiI3NWRhYTgwNzY4ZDc2ZDdiODJkNTkzODcxYzlkOTIxNjY0YmFkY2E4MTc2YzFmNDE5NDAwMGUxNGEyN2Y4YjM3In0='
    })
soup = BeautifulSoup(r1.text,'html.parser')
for b2 in soup.find_all('div',{'class':'flex justify-between'}): 
  print("食譜名:", b2.find('a',{'class':'block-link__main'}).text.strip(), "\n",
    "URL:", f"https://cookpad.com/{b2.find('a').attrs['href']}"           )
  rName = b2.find('a',{'class':'block-link__main'}).text.strip()
  # print(rName)
  r2 = requests.get(f"https://cookpad.com/tw/食譜/{rName}?ref=search&search_term={ingredient}",
        headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'cookie':'ab_session=0.22805529257603352; f_unique_id=6efac12f-8eab-4f3d-acf3-a23a1f8f1d91; _pxhd=TovEuEN-xfV7Ar0YHtuH3Qr-sTTLjOPog6ablRteoLQ7ZIj06a6KEefxj/2ztcbi9m68-CCc29bxWOWlA0Fx9g==:/csEACcDK0GMfB/75dfhxJ11vmXScRu1SgEvSGuHYrD6uCIMOlbYdtmcm4UJmp8yP0f8iRvo5hlNvgfvPbyucF13t6nhL2QIjpMaG-RJh9649tJmImHzvdWfudqfPsGXap86XcjcWqIyeQ4BHreaeg==; _ga=GA1.2.2007734559.1640229926; _gid=GA1.2.1789152356.1640229926; pxcts=f93458b0-639f-11ec-949e-19083dd0c3d0; _pxvid=f7e01d6a-639f-11ec-85d3-447563516857; keyword_history_zh-TW=%5B%22%E7%89%9B%E8%82%89%22%5D; accept_cookies_and_privacy_and_terms=1; recipe_view_count_zh-TW=1; _global_web_session=o%2BvjLGo9kq769UhZik7iIFo6in%2F8HXTz%2Fd60sMvuaXYPErahI3Vj8Uo32UPPh4uiCVD2KYJGTUUQffLoB8OX88suAaPki0PgYFnSavzjZGu2wpTZUb80So2wUVCrhZW8kBp5oUbLynTkHDW8UFYrR3uX2PRA781WMGsVoaYK4LGZtiHGnOQeSMg4WsPpOT56kAOzf95YPeX6BE4oV%2FCuEiMm11lgs9oGlg1hXrOFYPE2fwqmohthK7l8yYQC8zTmCqCKsqjzY2Mv63T76mPeAaGIhXNKPfhP4mZI6wNjxapR%2FastdoayXbSXNGIywnOFU1Myg75FgwLy3bESTxeJ--zY0cxzTt2vhOeqMk--qmYD2%2BrCkbL32%2Fg5F6Fqhw%3D%3D; _px2=eyJ1IjoiZjgxZDZhNzAtNjM5Zi0xMWVjLTlkMjgtYjcwMGE1M2ZkODc5IiwidiI6ImY3ZTAxZDZhLTYzOWYtMTFlYy04NWQzLTQ0NzU2MzUxNjg1NyIsInQiOjE2NDAyMzA0NjkxNzcsImgiOiI3NWRhYTgwNzY4ZDc2ZDdiODJkNTkzODcxYzlkOTIxNjY0YmFkY2E4MTc2YzFmNDE5NDAwMGUxNGEyN2Y4YjM3In0='
    })
  soup2 = BeautifulSoup(r2.text,'html.parser')
  # print(soup2)
  for img in soup2.find_all('div',{'class':'tofu_image'}):
    img_src = img.find('img').attrs['src'].split('.')
    # print(img_src)
    img_url = f"https://cookpad.com/tw/recipe/images/{img_src[1]}"
    # print(img_url)
