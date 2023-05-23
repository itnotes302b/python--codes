import pandas as pd
name = {1:'rama',2:'hitesh ',3:'piyush',4:'im' }
surname={1:'Rajbhar',2:'Mistry',3:'Sarang',5:'fm' }
data = {'firstname':name ,'Surname':surname}
a=pd.Series(data)
print("First trying using pd.series : \n " ,a)
a=pd.DataFrame(data)
print("Now trying using DATAFRAMES :\n ", a)
print("THe difference is series print in series only and \n dataframes "
      "show o/p in two dimentional structure ")

import numpy as np
n1=np.array([[1,2,3,4],[10,11,12,13]])
n=pd.DataFrame(n1) # DATAFRAME  show 2d structure hence we can pass 2darray as data in it
# AND BYDEFAULT it will do indexing
print(n)

roll=pd.Series([1,2,3,4])
age=pd.Series([17,18,19,20])
marks=pd.Series([12,13,14,15])
total={'RollNO':roll,'AGE':age,'MARKS':marks}
m=pd.DataFrame(total)
print(m)
# I can also add index ike this
m.index=['A','B','C','D']
print(m)

'''Reading CSV file using pandas'''
c=pd.read_csv('lan.csv')
print("Reading csv file ",c)
