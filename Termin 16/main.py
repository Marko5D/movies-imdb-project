import pandas as pd

data1 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
data2 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

result = data1 * data2

print(result)