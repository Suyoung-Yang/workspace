"""

"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import FinanceDataReader as fdr

# 원하는 정보 입력
# item, start, end = input().strip().split(" ")
# df = fdr.DataReader(item,start=start,end=end)

# # 상장종목 가져오기
# def getKRXList():
#     df = pd.read_csv("C:/Users/Yang/workspace/FinanceData/krx.csv")
#     df_KRX = df[["Name","Symbol"]]
#     # df_KRX_Total = fdr.StockListing('KRX')
#
#     return df_KRX
#
#
# # 종목명으로 종목 코드 받아오는 함수 만들기
# def item_code_by_item_name(item_name):
#     item_code_list = getKRXList().loc[getKRXList()["Name"]==item_name,"Symbol"].tolist()
#
#
df = pd.read_csv("C:/Users/Yang/workspace/FinanceData/krx.csv")
df_KRX = df[["Name","Symbol"]]

#종목명으로 종목 코드 받아오기
item_name = input()
item_code = df_KRX.loc[df_KRX["Name"]==item_name,"Symbol"].tolist()[0]
year = 2020

# 종목명으로 일별시세 받아오기
df_day = fdr.DataReader(item_code,str(year))

# 시각화하기
# fig1 = df_day.plot()
df_day.plot(figsize=(30,10))


g = df_day.plot(subplots=True,figsize = (20,10))


h = df_day.hist(figsize=(30,10),bins=20)

df_day[["Close","Volume"]].plot(figsize=(30,10), secondary_y="Volume")
