import pandas as pd 
path = 'db\\WEOOct2023all.xlsx'

#pip install pandas openpyxl
#pip install pandas xlrd
df = pd.read_excel(path)
#df = pd.read_csv(path)
print(df)

select = ['WEO Country Code','Country']
subset = df[select]
print(subset)

path_csv = 'db\\oecd_bli_2022.csv'
df = pd.read_csv(path_csv)
print(df)
df.to_excel('db\\oecd_bli_2022.xlsx', index=False)


ver pg 43/564