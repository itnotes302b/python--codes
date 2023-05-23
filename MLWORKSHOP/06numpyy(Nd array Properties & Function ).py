import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype='float32')
print(a , "shape of array is ",a.shape)
print("Dimension of array is ",a.ndim, "The size of array is " ,a.size )
# Arthimetic Mean AM = x1+x2+x3...xn / n
print( "Arithmetic Mean is :", a.mean())

print(" principal diagonal " ,a.diagonal())
print(" maximum value in matrix" , a.max()) #also np.max(a)
print("minimum value ", a.min())
print(" multilplicatiion of all elements is " , a.prod())
print(" Resize of array " , a.reshape([9,1]))
print("sum of all elements ", a.sum())
print("Transpose of matrix " , a.transpose()) #value of  rows are converted into column and column comes in rows
print("Trace : it add the element of principal diagonal", a.trace())

b=np.array([[10,20,30],[40,50,60]],dtype='float32')
print(b , "size of second array is is",b.size )
print("shape of second array is : ",b.shape)
b.resize((3,3))
b[2]=np.array([70,80,90])
print(b)
print("addition of two matrix ie A and B : ", a+b)
print("subtraction of two matrix ie A and B : ", a-b)
print("addition of two value 2 in A : ", a+2)
print("Multiplication of two matrix ie : 1st row * 1st column like that  ", np.matmul(a,b))
#if it is square matrix we cam also claculate determinant
print("Determinant of matrix A is :", np.linalg.det(a))
print("mean is ",a.mean())
print("average is  ",np.average(a))
print("standard devation :",np.std(a))
print("varation is ",np.var(a))


x=np.genfromtxt('data.txt',delimiter=',')
print(x)
x=x.astype('int32')
print(x)
