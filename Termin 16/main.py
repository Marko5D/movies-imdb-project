import pandas as pd

df = pd.read_xml('movies.xml', parser="etree")

print(df)