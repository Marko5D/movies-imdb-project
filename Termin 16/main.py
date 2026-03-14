import pandas as pd

df = pd.read_xml('movies.xml', parser="etree")

for i, value in df.iterrows():
    print(value)