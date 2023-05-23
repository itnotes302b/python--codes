# In Pie chart ARC Length of each slice is propertional tothe Quantity it Present
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt
def avg(l):
    s=0
    for i in l:
        s=s+i
        a=s/len(l)
        return a

days=[1,2,3,4,5,6,7]
sleeping=[6,8,7,5,9,4,5]
study=[3,4,5,1,2,3,7]
exercise=[1,2,3,3,2,1,0]
phone=[4,5,6,3,5,3,9]
other=[6,7,4,5,6,3,4]
activities=['sleeping','study','exercise','phone','other']
hrs=[avg(sleeping),avg(study),avg(exercise),avg(phone),avg(other)]
clr=['m','c','r','g','b']

plt.pie(hrs,labels=activities,colors=clr,explode=(0,0,0,0.2,0),autopct='%6.2f%%')
# exploid (values , values) menas pie kitne bahar ana  chayea
# autopct = '%2.2%'  %% is a format 2.2 means kine numbers tak point mai dikna chayea 1more % is for print

plt.title('PIE CHARTS')
plt.legend()
plt.show()
#print(help(plt.pie))
