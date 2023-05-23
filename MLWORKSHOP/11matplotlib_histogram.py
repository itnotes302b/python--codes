# A Histogram is a BarGraph of Raw Data that craete a pictureof the Data Distribution
from matplotlib import pyplot as plt
test=[1,2,3,4,5,6,7,8,9]
m1=[14,21,40,60,90,30,70,20,50]
#m2=[90,80,70,60,50,30,80,20,45]
bins=[0,20,40,60,80]
plt.hist(m1,bins,histtype='bar',rwidth=1)
plt.xlabel("Marks")
plt.ylabel("No of Test")
plt.title("test score")
plt.show()
print(help(plt.hist))