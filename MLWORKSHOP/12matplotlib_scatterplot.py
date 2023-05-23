# Scatter Plot is a type of data display that shoe the  relationship between two numberical values
from matplotlib import pyplot as plt
test=[1,2,3,4,5,6,7,8,9]
m1=[14,21,40,60,90,30,70,20,50]
m2=[90,80,70,60,50,30,80,20,45]
plt.scatter(test,m1,label='ramashish',color='c',marker='*',s=100)
plt.scatter(test , m2 , label='jack', s=100)
plt.ylabel('Test Marks')
plt.xlabel('No of Test ')
plt.title('Test Score')
plt.legend()
plt.show()
