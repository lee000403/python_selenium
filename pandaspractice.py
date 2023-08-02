import pandas as pd
import numpy as np

# df = pd.Series([3, 5, 7, 9, 11], dtype=float)
# print(df) 

# df = pd.Series(["가", "나", "다", "라", "마"], dtype=object)
# print(df)

# sample = pd.Series([10,20,30,40,50], index=["가", "나", "다", "라", "마"], dtype=int)
# print(sample)
# print(sample[1:4:2])

# np.random.seed(20)
# sample2 = pd.Series(np.random.randint(100, 200, size=(15,)))
# sample2 <= 160
# print(sample2[sample2<=160])
# print(sample2[sample2[sample2<=170] & sample2[sample2>=130]])

# fruit = pd.Series(["apple", np.NaN, "banana", "kiwi", "gubong"], index=["가", "나", "다", "라", "마"], dtype=object)
# print(fruit)

# sample = pd.Series(['IT서비스', np.nan, '반도체', np.nan, '바이오', '자율주행'])
# print(sample[sample.notnull()])

# np.random.seed(0)
# sample = pd.Series(np.random.randint(100, 200, size=(10,)))
# print(sample[2:7])

# np.random.seed(0)
# sample2 = pd.Series(np.random.randint(100, 200, size=(10,)), index=list('가나다라마바사아자차'))
# print(sample2["바" : "차"])
# print(sample2["가" :"다"])
# print(sample2["나" : "바"])

df = pd.read_excel("C:\Users\5-18\Downloads\Polls.csv", encoding="utf-8")
print(df)