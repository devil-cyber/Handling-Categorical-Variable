import pandas as pd
c=['m','p']
data=pd.read_csv('data.csv')
l=pd.get_dummies(data[c])

print(l)