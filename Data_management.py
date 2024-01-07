# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 15:27:01 2024

@author: ahmed.abdelmonim
"""
import pandas as pd 
import datetime as dt

df = pd.read_csv('ExportSales.csv')

# derived variables used for customer segmentation 
# Total_Sales : Toatal sales
# Number of unique Purchase 
# Number of unique products 
# Number of unique Category
# Number of unique Destenation
df.columns
# create Month and Year variables 
df['Date']= pd.to_datetime(df['Date'],format="%d/%m/%Y")
df['Month']= df['Date'].dt.month
df['Year']= df['Date'].dt.year

# Total_Sales
df1 = df.groupby(['Customer Code'])['Total Price'].sum().reset_index()
df1.rename(columns = {'Total Price':'Total Sales'} ,inplace = True)

#Number of unique Purchase 
df2 = df.groupby(['Customer Code'])['Invoice Number'].nunique().reset_index()
df2.rename(columns = {'Invoice Number' : 'buying_freq'},inplace = True)

#Products Eng
df3 = df.groupby(['Customer Code'])['Product Code'].nunique().reset_index()
df3.rename(columns = {'Product Code': 'Products_Eng'},inplace = True)
#Category Eng
df4 = df.groupby(['Customer Code'])['Category'].nunique().reset_index()
df4.rename(columns = {'Category': 'Category_Eng'},inplace = True)

# Number of unique Destenation
df5 = df.groupby(['Customer Code'])['Destenation'].nunique().reset_index()
df5.rename(columns = {'Destenation': 'Destenation_Eng'},inplace = True)

# marging all the above dfs
finaldf = pd.merge(pd.merge(pd.merge(pd.merge(df1,df2,on = ['Customer Code'],how = 'outer' ),
df3,on = ['Customer Code'],how = 'outer'),df4,on = ['Customer Code'],how = 'outer'),df5,on = ['Customer Code'],how = 'outer')

# replace Nan value with 0 since NA 
finaldf = finaldf.fillna(0)

finaldf.to_csv('finaldf.csv')










