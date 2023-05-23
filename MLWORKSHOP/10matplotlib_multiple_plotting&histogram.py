from matplotlib import pyplot as plt
test=[1,2,3,4,5]
s1=[80,90,30,40,90]
s2=[15,20,60,80,10]
#it's graph
'''plt.plot(test,s1,label='abhishekh')
plt.plot(test,s2,label='ramashish')'''

#It's histogram
'''
plt.bar(test,s1,label='abhishekh') # showing bar single data
# If s2 marks id greater than s1 then it will hide in graph Hence use single data
plt.bar(test,s2,label='ramashish')
'''

# If we want multiple data in proper adjacentformat then following steps
'''
plt.bar([i+0.2 for i in test],s1,label='abhishekh')
plt.bar([i-0.2 for i in test],s2,label='ramashish')
'''
# here we shift some lines using list compresion
# Now we control some width to show properly
plt.bar([i+0.1 for i in test],s1,width=0.2,label='abhishekh')
plt.bar([i-0.1 for i in test],s2,width=0.2,label='ramashish')

plt.xlabel('Test')
plt.ylabel('Marks')
plt.title('Student Score')
plt.legend()
plt.show()