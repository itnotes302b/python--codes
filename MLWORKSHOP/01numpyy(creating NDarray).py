import numpy as np
a=np.array([1,2,3])
print(a, type(a))
b=np.array([[1,2,3],[10,20,30]]) #multi dimentional array
print(b)
q=np.array([[1,2,3],[10,20]])  # here numpy is considering that is one dimentional array in which first and second element is the list
print(q)
# array are homogeneous (same type of element ) in above example both type is list
# but below example is also comsiderable because in numpy list is object and string is also object hence it is considerable
c=np.array([[1,2,3],"hello "])
print(c)
d=np.array([[1,2,3], 30])
print(d)
#in below example it will not throw error but it will make all element as float
e=np.array([[1,2,3.0],[10,20,30]])
print(e)
#in below example it will not throw error but it will make all element as string
f=np.array([[1,2,3],[10,'a',30]])
print(f)