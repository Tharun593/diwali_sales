import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

diwali_data = pd.read_csv(r'Diwali Sales Data.csv',encoding='unicode_escape')
# print(diwali_data)
# print(diwali_data.shape)
# print(diwali_data.head())
# print(diwali_data.tail())
# print(diwali_data.index)
# print(diwali_data.columns)
# print(diwali_data.info())
# print(diwali_data.describe())
# print(diwali_data)
# print(diwali_data.head(10))
# a=diwali_data['State']
# print(a)
# null_data = diwali_data.isnull()
# count_of_null = null_data.sum()
# print(count_of_null.count())
# col_count = diwali_data.columns.value_counts()
# print(col_count)
# val_counts = diwali_data.value_counts().head()
# print(val_counts)
# print(diwali_data.value_counts)
# pro_cat = diwali_data['Product_Category'].value_counts()
# print(pro_cat)
# print(pro_cat.head())
# pro_id = diwali_data[diwali_data['Product_ID']=='P00110942'] 
# print(pro_id.count().sum())
# nulls = diwali_data.isnull()
# high = nulls.sum()
# print(high.notnull())
# print(high.bool)
# cust_name = diwali_data[diwali_data['Cust_name']==('Sanskriti' and 'P00030942')]
# print(cust_name)
# diwali_data.drop(['Status','unnamed1'],axis=1,inplace=True)
# print(diwali_data.head())
# diwali_data[diwali_data.isnull()]
# print(diwali_data)
# diwali_data.dropna(axis=1,inplace=True)
# print(diwali_data.head())
# nulls = pd.isnull(diwali_data).sum()
# print(nulls)
# row_name = diwali_data.rename(columns={'Marital_Status':'Shaadi'})
# print(row_name.head())
# sort =  diwali_data[['Age','Orders','Amount']].describe()
# print(sort)
# x=diwali_data.describe()
# print(x)
# ax = sns.countplot(x='Gender',data=diwali_data)

# for bar in ax.containers:
#     ax.bar_label(bar)

# ax = sns.countplot(x = 'Gender',data = diwali_data)

# for bars in ax.containers:
#     print(ax.bar_label(bars))

# plt.show()

# print(diwali_data.columns)

# sales_gen = diwali_data.groupby(['Gender'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
# sns.barplot(x='Gender',y='Orders',data=sales_gen)
# plt.show()

# xa = sns.countplot(data=diwali_data , x= 'Age Group' , hue='Gender')

# for bars in xa.containers:
#     xa.bar_label(bars)

# plt.show()

