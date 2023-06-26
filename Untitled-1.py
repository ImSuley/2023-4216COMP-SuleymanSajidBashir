
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 


df=pd.read_csv('billionaires.csv')
df

subSet = df[['Rank','Name', 'Demographics Gender', 'Year', 'Company Name', 'Company Sector', 'Wealth How Inherited' ]] 

subSet = subSet.rename({'Wealth How Inherited': 'Was the Wealth Inherited?',
                        'Demographics Gender': 'Gender'                                
}, axis=1)


subSet

subSet.dropna() # Cleaning Data to remove null values

subSet.head(25)


Gender_counts=subSet['Gender'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(Gender_counts,labels=Gender_counts.index,autopct='%1.1f%%')
plt.title('Gender Ratio')  
plt.axis('on')
plt.show()