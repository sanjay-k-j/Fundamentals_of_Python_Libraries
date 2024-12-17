import pandas as pd

# ser = pd.Series(["p","q","r"],dtype="category")

# print("\n Display the series : \n", ser)


df = pd.DataFrame({"Cat1" : list("pqrs"),"Cat2" : list("pqrs"),"Cat3":list("pqrs"),"Cat4":list("pqrs")}, dtype="category")

print(df)