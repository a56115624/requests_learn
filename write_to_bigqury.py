""" 嘗試將簡單的資料寫進bigqury資料庫
如果嘗試將爬蟲的結果寫入資料庫,請參考這段 """


from random import shuffle
import os
from google.cloud import bigquery as bq
from linebot.models import TextSendMessage
import os
from google.cloud import storage
from google.cloud import bigquery 
import pandas as pd
#環境變數
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/ratatouille-ai-e6daa9d44a92.json"

client = bq.Client()
#要使用sql指令
QUERY = "INSERT INTO `ratatouille-ai.shane.recipet_to_mvp`(`id`, `name`, `URL`,  `ingredient_main`, `igredient_other`, `seasoning`) VALUES (0, '0', '0', '0', '0', '0')"


job = client.query(QUERY)
job.result()


print("已存入")






