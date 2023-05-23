import numpy as np
a=np.array([[1,2,3],[10,20,10]], dtype='int16')
print("array are",+a,"dimention of array are ",+ a.ndim)
print("accesing array element ",+a[0][0], "second element ",+a[0][1])
print("accesing array element using a[1,2]",+a[1,2])
print("accesing 1st row of array ",+a[0] , "accesing 2dn elemrnt ",+a[1])
a[0,0]=9
print(a)
a[1]=[10,20,30]
print(a)
print("")

"""# let's learn about slicing
# beginnig : end : step(bydefault it is 1 )
# eg : 2:5:1  o/p 2,3,4
# eg : 2:8:2  o/p 2,4,6,8 . """

# for accesing columns we use sclicing
print(a[::,0]) # :: selects all rows and columns
print(a[::,1]) # accesing 2 nd column
print(a[::,2])
#here in below example 2 or last row is selected but 3or last coloum will not come
#last row will print without last or 3rd column
print(a[1::,:2])

