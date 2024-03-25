'''
Examplo 1-1. traning and running a linear model using Scikit-learn
'''

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
import sklearn

# Load the data
path = 'db\\WEOOct2023all.xlsx'
df = pd.read_excel(path)
#df = pd.read_csv(path)
print(df)

path = 'db\\oecd_bli_2022.xlsx'
df1 = pd.read_excel(path)

#select = ['GDP per capita','Life satisfaction']
#subset = df[select]
#print(subset)

#select = [0,1,2,3,4,5]
#subset = df.iloc[:,select]
#print(subset)

print("\n Lista de nomes das colunas df")
column_name = list(df.columns)
print(column_name)

print("\n Lista de nomes das colunas df1")
column_name = list(df1.columns)
print(column_name)

print("\n")
print(df1)

select = ['Country','Value', 'Unit Code', 'Unit']
subset = df1[select]
print(subset)

# Agrupa por 'Country' e soma os valores
#sum_by_country = subset.groupby('Country')['Value'].sum().reset_index()

# Imprime o resultado
#print(sum_by_country)

# Agrupa por 'Country' e media dos valores
average_by_country = subset.groupby('Country')['Value'].mean().reset_index()

# Imprime o resultado
print(average_by_country)

#Atenção estava difícil aplicar o exemplo com o dataset do db
#Criamos um manualmente na variavel data
#Ao desenvolver mais a manipulação de dados será mais simplis aplicar o modelo com dados reais.

# Supondo que 'df1' seja o seu DataFrame
data = {'Country': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
        'Value': [10, 20, 30, 40, 50, 60, 70, 80],
        'Unit Code': [1, 2, 1, 2, 1, 1, 2, 2],
        'Unit': ['kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg', 'kg'],
        'GDP per capita': [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000],
        'Life satisfaction': [5, 6, 7, 8, 9, 9, 9.4, 9.5]}

df1 = pd.DataFrame(data)

# Prepare the data
X = np.c_[df1["GDP per capita"]]
y = np.c_[df1["Life satisfaction"]]

# Visualize the data
df1.plot(kind='scatter', x="GDP per capita", y='Life satisfaction', title='GDP per capita vs. Life satisfaction')
plt.show()

# Select a linear model
from sklearn.linear_model import LinearRegression
lin_reg_model = LinearRegression()

# Train the model
lin_reg_model.fit(X, y)

# Make a prediction for a new GDP per capita value
X_new = [[22587]]  # Cyprus' GDP per capita
predicted_life_satisfaction = lin_reg_model.predict(X_new)
print("Predicted Life Satisfaction:", predicted_life_satisfaction[0, 0])

#In summary:
##  You studied the data.
##  You selected a model.
##  You trained it on the training data.
##  You applied the model to make predictions on new cases (inference).
###     This is what a typical Machine Learning project looks like.


