# Введите ваше решение ниже
import pandas as pd
df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] >=0) & (df['population'] <=500)]['median_house_value'].mean()
#print(avg)