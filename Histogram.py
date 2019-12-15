mport matplotlib.pyplot as plt
population_ages = [7,11,15,22,25,27,33,34,35,39,44,43,48,51,50,58,56,67,65,66,63,62,73,71,88,86,96,97,90,101,105,110]
bins=[0,10,20,30,40,50,60,70,80,90,100,110]

plt.hist(population_ages,bins,histtype = 'bar',rwidth=0.8)
plt.xlabel('P')
plt.ylabel('Q')
plt.title('Graph')

plt.legend()
plt.show()
