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

cat = CategoricalFeature(df, categorical_features=c, encoding_type='ohe', handle_na=True)
cat.fit_transform() #This will return the transformed value of the dataset
```
```
For  a input like this:
    m     n     p
0 india  1000  rav1
1 us     2000  mani
2 japan  3000  ravi
3 us     4000  shri
4 japan  5000  shri


Output will look like this:
      n  m__bin_0  m__bin_1  m__bin_2  p__bin_0  p__bin_1  p__bin_2  p__bin_3
0  1000         1         0         0         0         1         0         0
1  2000         0         0         1         1         0         0         0
2  3000         0         1         0         0         0         1         0
3  4000         0         0         1         0         0         0         1
4  5000         0         1         0         0         0         0         1


```
 
By. Manikant Kumar
