import pandas as pd

print(pd.__version__)

s1 = pd.Series([1, 3, 5], index = [10, 20, 30])
print(type(s1))
print(s1)
