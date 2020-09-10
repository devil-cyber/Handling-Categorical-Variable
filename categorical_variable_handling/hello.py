import pandas as pd
from categorical_variable_handling import CategoricalFeature

c=['m','p']
data=pd.read_csv('data.csv')
cat=CategoricalFeature(data,categorical_features=c,encoding_type='binary',handle_na=True)
output=cat.fit_transform()

print(output)