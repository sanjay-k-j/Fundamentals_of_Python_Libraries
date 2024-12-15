import pandas as pd
# create a dataframe
data = {
    "Student" : ["Sanjay", "Ajay", "Vijay","Puneeth"],
    'Rank' : [2,3,1,4],
    'Marks':[92,87,99,80]
}
df = pd.DataFrame(data)

print(df)


# access the value using Rows and Columns 
# use index Argument for indexing the df
df2 = pd.DataFrame(data,index=["RowA",'RowB','RowC','RowD'])

print("\nStudent Records\n\n",df2)

print("\nValue of A and Column Student is : ",df2.loc['RowA','Student'])

# Access the Group of Rows or columns using the integer position

print("The value of 2nd and 3rd row in the python index is (1,2):\n",df2.iloc[[1,2]])


print("\n\nIterate the Columns\n\n")
# Display the columns 
for col in df :
    print(col)

