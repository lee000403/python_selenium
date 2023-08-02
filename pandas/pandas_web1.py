import pandas as pd
import numpy as np
import csv

data_web = pd.read_csv("sise.csv", encoding="UTF-8-sig")
df = pd.DataFrame(data_web)
print(df)
df.rename(columns={"N" : "번호"}, inplace=True)
df_drop = df.loc[:, "전일비": ]
df.drop(df_drop, axis=1 , inplace=True)
df_change = df.loc[:, ["번호"]]
# print(df_change)
df.drop(df_change, axis=1, inplace=True)
print(df_drop)
# print(df)
# print(df[df["현재가"] > 780000].loc[:, ["종목명", "현재가"]])
# print(df[df["종목명"].str.contains("삼")])
# print(df.loc[df["현재가"].idxmax()])
# print(df[["종목명", "현재가"]].sort_values("현재가", ascending=False))
# print(df.loc[2])

df.to_csv("./sise_name.csv")