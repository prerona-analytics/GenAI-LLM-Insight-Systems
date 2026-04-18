import pandas as pd
df = pd.read_csv('data/sales_data.csv')
print(df.groupby(['Region','Category'])['Revenue'].sum())
