 **Categorical Variable handling**<br>
* This is a package that contain some powerful Categorical feature handling algorithm :
* For that you have to install this library using pip command 
* Then observe you dataset and figure out which encoding technique you wants to used
* After that call that library and do as follows:
```python
from categorical_variable _handling import CategoricalFeature
column="Give here the list of Categorical column"
dataframe="Here give the dataframe"
encoding_type="Here give the encoding type e.g:'label','binary','ohe':one hot encoder"
handle_na="this is a boolean value if you wants to handle the NaN value then make true else make false "

cat = CategoricalFeature(df, categorical_features=c, encoding_type='ohe', handle_na=True
cat.fit_transform() #This will return the transformed value of the dataset
```
 
By. Manikant Kumar
