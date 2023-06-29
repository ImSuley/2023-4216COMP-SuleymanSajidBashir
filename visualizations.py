
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt        #importing my libaries
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'vscode'
pio.templates.default = 'plotly'

df=pd.read_csv('billionaires.csv')  #loading my dataset
df

subSet = df[['Rank','Name', 'Demographics Gender', 'Year', 'Company Name', 'Company Sector', 'Wealth How Inherited' ]] 

subSet = subSet.rename({'Wealth How Inherited': 'Was the Wealth Inherited?',
                        'Demographics Gender': 'Gender'                 }, axis=1)

subSet

subSet.dropna()  #cleaning data to remove null values
subSet.head(25)     


Gender_counts=subSet['Gender'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(Gender_counts,labels=Gender_counts.index,autopct='%1.1f%%')          #pie chart for the gener
plt.title('Gender Ratio')  
plt.axis('on')
plt.show()




Wealth_How_Industry = df['Wealth How Industry'].unique()
age_by_wealth = df.groupby('Wealth How Industry')['Demographics Age'].mean().dropna()

plt.bar(age_by_wealth.index, age_by_wealth, color='green')
plt.xlabel('Wealth How Industry')
plt.ylabel('Age')                                                              #bar graph for the age distribution by Wealth How Industry
plt.title('Age Distribution by Wealth How Industry')
plt.xticks(rotation=45)
plt.show()

Wealth_How_Inherited=subSet['Was the Wealth Inherited?'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(Wealth_How_Inherited,labels=Wealth_How_Inherited.index,autopct='%1.1f%%')
plt.title('Was the Wealth Inherited?')                                                    #pie chart for if the wealth was inherited
plt.axis('on')
plt.show()


