import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])
data2 = pd.Series([10, 20, 30, 40, 50])

result = data * data2

print(result)