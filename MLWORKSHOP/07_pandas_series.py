import  pandas as pd
data=['Mumbai','Jalgaon','Benguluru','Chennai','Delhi ','Bandra']
index=['M','J','B','C','D','B']
a=pd.Series(data , index)
print(a) # we take data in form of list
# now tuple and yes it will work
data='Mumbai','Jalgaon','Benguluru','Chennai','Delhi ','Bandra'
index=['M','J','B','C','D','B']
a=pd.Series(data , index)
print(a)

b1=1,2,3,3,4,5
b=pd.Series(b1) # If index is not given then bydefult it will start from 0
print(b)

#there can be hetrogeneous values but datatype become object in above ex dataype is int32
# It will treat all hetrogeneous values as object
c1=1,2,3,3.3,4.4,5,'prajal'
c=pd.Series(c1)
print(c)

# NOw Using Dictionart
d1={1:'Mumbai',2:'Jalgaon',3:'Benguluru',4:'Chennai',5:'Delhi ',6:'Bandra'}
d=pd.Series(d1) # No need of index because of dictionary key-value pair
print(d)

# Now USing numpy
import  numpy as np
X1=np.array([[1,2,3],[11,22,33]])
X2=np.array([[10,20,30],[101,102,103]])
index_i=0,1
data_d=X1,X2
N=pd.Series(data_d,index_i)
print(N)
"""IMP PONTS TO REMEMBER 
IF u pass N=pd.Series(X1) #which is 2dimentional array 
Then it will throw error 
but if data= X1 then its is ok 
becauese you are not passing 2darray
X1 contains  2darray 
//Little confusing na ?

Data = data is a collection of values
in our case data_d 
data_d is collection of values X1, X2 
the values individually may be 2d,3d array no problem 
But data/data_d should not be 2d array  
hence value pass in padas.Series never be 2d array """

