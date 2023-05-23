# A Stack Plot is a plot that show the whole data set with easy visulation
# of how each part make up the whole . Eacch constiuent of Stack Plot is stacked on each other
# It shows the part make up of the unit as well as the whole unit
from matplotlib import pyplot as plt
days=[1,2,3,4,5,6,7]
sleeping=[6,8,7,5,9,4,5]
study=[3,4,5,1,2,3,7]
exercise=[1,2,3,3,2,1,0]
phone=[4,5,6,3,5,3,9]
other=[6,7,4,5,6,3,4]
labs=['sleeping','study','exercise','phone','other']
clr=['m','c','r','k','b']
plt.stackplot(days,sleeping,study,exercise,phone,other,labels=labs,colors=clr)

plt.xlabel('days')
plt.ylabel('activities')
plt.title('Performance')
plt.legend()
plt.show()
