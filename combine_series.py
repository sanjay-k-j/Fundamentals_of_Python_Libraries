import pandas as pd
# combine 2 series of pandas

data = [10,20,32,122,50]
data2 = [453,23,10,100,34]

print(pd.Series(data))

series1 = pd.Series(data)
series2 = pd.Series(data2)

def demo(x1,x2):
    return x1 if x1 > x2 else x2 

res = series1.combine(series2, demo)
print("\n After Combining\n",res)