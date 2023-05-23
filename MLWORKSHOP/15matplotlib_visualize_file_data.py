from matplotlib import pyplot as plt
import csv
test=[]
marks=[]
with open( 'data1.txt' , 'r') as file :


    c=csv.reader(file,delimiter=',')
    for row in c :
         test.append(int(row[0]))
         marks.append(int(row[1]))

plt.plot(test,marks,label='Load From Files ')
plt.title('Display File Data')
plt.show()