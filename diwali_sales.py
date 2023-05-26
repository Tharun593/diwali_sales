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

# x=lambda a: a*a
# print(x(5))

# a=[x for x in range(5)]
# print(a)

# a=10
# print(a)
# print()

# x=lambda a: a**a
# print(x(2))

# def sum(a,b):
#     return a+b
# print(sum(2,3))

# class Tharun:
#     def __init__(self,name,age,gender,address,phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.address = address
#         self.phone = phone
#     def display(self):
#         print('The name:',self.name)
#         print('The age:',self.age)
#         print('The gender:',self.gender)
#         print('The address:',self.address)
#         print('The phone:',self.phone)
# print()
# s = Tharun('Tharun',29,'Male','Hyderabad',9490541278)
# s.display()
# print()

class Worker:
    location_name = 'Hyderabad'
    
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def show(self):
        print('Worker name: ', self.name,',',self.id)
        print('Worker location: ', self.location_name)
    
    @classmethod
    def change_location(cls,location):
        print('Previous location name: ', cls.location_name)
        cls.location_name=location
        print('After changing location: ', cls.location_name)
    
    @staticmethod
    def tool_box():
        return['tool1','tool2','tool3']

c = Worker('Tharun',1234)
c.show()
c.change_location('Vijayawada')
print(c.tool_box())