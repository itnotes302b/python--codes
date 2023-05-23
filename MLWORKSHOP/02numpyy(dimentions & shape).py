import numpy as np
a=np.array([1,2,3])
b=np.array([[1,2,3],[10,20,30]]) #multi dimentional array
c=np.array([ [ [1,2,3] , [10,20,30] ] , [ [2,3,33] , [3,3,3]  ]  ] )
print(a)
print(a.ndim)
print(" shape is ", a.shape)
print(b, b.ndim)
print("shape is :",b.shape)
print("")
print(c, c.ndim)
print("shape is : ",c.shape)

