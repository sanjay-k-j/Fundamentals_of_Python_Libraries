import pandas as pd
import numpy as np

# series

data = [10,20,30,40,50,np.nan]

s= pd.Series(data,name="My series name")

print(s[2])

print("\n",s)

# how to access value using custom index

# print("\n The value od row4 is : ",s["Row4"]) 
# attributes in Series (1D array)
# print(s.ndim)
# print(s.size)
# print(s.name)
# has nan attributes
print(s.hasnans)
print(s.info())