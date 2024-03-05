'''
Whats is Machine Learning?
    Science (and art) of programming computers so they can learn from data.
Why Use Machine Learning?
    Problems for which existing solutions require a lot of hand-tuning or long lists of rules:
        one Machine Learning algorithm can often simplify code and perform better.
    Complex problems for which there is no good solution at all using a traditional aproach:
        the best Machine Learning techniques can find a solution.
    Fluctuating environments:
        a Machine Learning system can adapt to new data.
    Getting insights about complex problems and large amounts of data.
Types of Machine Learning Systems
    Supervised
    Unsupervised
    Semisupervised
    Reinforcement
'''


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


#pag. 43/564
#file:///L:/Linear_/Base-TI/Hands%20On%20Machine%20Learning%20with%20Scikit%20Learn%20and%20TensorFlow.pdf