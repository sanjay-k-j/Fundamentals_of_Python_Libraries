import pandas as pd

# ser = pd.Series(["p","q","r"],dtype="category")

# print("\n Display the series : \n", ser)


df = pd.DataFrame({"Cat1" : list("abc"),"Cat2" : list("xyz"),"Cat3":list("pqr"),"Cat4":list("abc")}, dtype="category")

print(df)