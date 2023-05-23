import numpy as np
a=np.array([1,2,3])
print(a)
print(,a.dtype)
a=np.array([1,2,3],dtype='int32')
print(a,a.dtype)
a=a.astype('float32') #changing data type in numpy
#a=np.array([1,2,3])
print(a,a.dtype)
l1=a.tolist() #converting array into list
print(a,type(l1))

# DATA TYPES IN NUMPY
"""np.int8
np.int16
np.int32
np.int64
np.uint8
np.uint16
np.uint32
np.uint64
np.float32
np.float64
np.complex64
np.complex128
"""