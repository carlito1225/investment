import pandas as pd
#綜合練習 1
#請求出s.rolling(2).sum().cumsum()+1的最大值
s = pd.Series([4, 7, -5 , 3])
print(s)
print(s.rolling(2).sum())
print(s.rolling(2).sum().cumsum())
print(s.rolling(2).sum().cumsum()+1)
print(s.shift())