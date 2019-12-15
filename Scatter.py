import matplotlib.pyplot as plt
x=[2,4,6,8,10,7,9]
y=[5,6,8,9,7,5,4]

plt.scatter(x,y,label='skitscat',color='b',s=150)
plt.xlabel('P')
plt.ylabel('Q')
plt.title('Graph')

plt.legend()
plt.show()
