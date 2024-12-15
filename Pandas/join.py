# Merges and Joins in Dataframes
import pandas as pd
# create a dataframe
data = {
    "Student" : ["Sanjay", "Ajay", "Vijay","Puneeth","hema",'suhas','jay'],
    'ID' : [2,3,1,4,5,10,35],
    'Marks':[92,87,99,80,64,95,63]
}

data2 = {
    "Names" : ["Jay","Sanjay","Vijay","hema","Vasu","rama"],
    'roll_id' : [43,2,1,5,435,34],
    "age" : [32,64,22,32,53,23]
}

df1 = pd.DataFrame(data)

df2 = pd.DataFrame(data2)

print("\nDataframe1:\n\n",df1)

print("\n\nDataframe2:\n\n",df2)

df3 = pd.merge(df1,df2,left_on=['Student','ID'],right_on=['Names','roll_id'])

print("\n\nDataframe joined : \n\n",df3)