mport matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[5,6,8,9,7]

x2=[1,3,5,7,9]
y2=[3,6,9,5,7]
plt.bar(x,y,label='Bars1',color='b')
plt.bar(x2,y2,label='Bars2',color='g')

plt.xlabel('P')
plt.ylabel('Q')
plt.title('Graph')

plt.legend()
plt.show()
