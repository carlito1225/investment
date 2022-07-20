import pandas as pd
'''
有一檔股票，20220701~07時價格=10元
          20220708~10時價格=15元  

'''
s = pd.Series(10, index=pd.date_range("20220701",periods=10))
print(s)
s.loc['2022-07-08':] +=5
print(s)