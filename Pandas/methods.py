# Attributes and Methods in Dataframes 
import pandas as pd
# create a dataframe
data = {
    "Student" : ["Sanjay", "Ajay", "Vijay","Puneeth"],
    'Rank' : [2,3,1,4],
    'Marks':[92,87,99,80]
}
# index =
df = pd.DataFrame(data,index= ["RowA","RowB","RowC","RowD"])

print(df)
# data typs of the columns
print("\nDataTypes\n\n",df.dtypes)


#using ndim attribute to check the dimention of dataframe
print("The dimention of the dataframe\n",df.ndim) 


# size attribute
print("Number of elements in the dataframe : ",df.size)


# shape attribute 
print("Shape of the dataframe: ",df.shape)

# index of the dataframe

print("\nIndex of the dataframe are\n",df.index)

# Transpose of the matrix 

print("Transpose of df\n\n",df.T)

# head method
print("\nhead method")
print(df.head(2))

# tail method

print("\nTail method\n")
print(df.tail(2))