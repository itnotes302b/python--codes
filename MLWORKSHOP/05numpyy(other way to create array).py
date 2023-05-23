import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='float32')
print(a)
a[1,1]=np.nan
print(a)
b=np.zeros((2,3))
print(b , b.dtype)
c=np.ones((3,4)) # matrix full with number 1 in given shape (rows, column )
print(c, c.dtype)
d=np.full((2,2),24) # full((shape ie:rows,column), number full the matrix)
print(d , d.dtype)

#identitiy matrix
"""in identity matric no of ROWS = no of COLUMNS 
and diagonal element is ONE 1 """
e=np.identity(3, dtype='int16')
print(e)

f=np.random.rand(3,4)
print(f)

g=np.random.randint(8,15,size=(3,4))
print(g)
