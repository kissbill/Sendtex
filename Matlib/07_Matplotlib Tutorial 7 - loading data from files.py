import matplotlib.pyplot as plt
import numpy as np



#Part 1
'''
import csv

x = []
y = []

with open('example.txt', 'r') as csvfile:
    plots = csv.reader(csvfile,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y, label= 'Loaded from file')
'''
#Part 2
x, y = np.loadtxt('example.txt', delimiter=',', unpack = True)
plt.plot(x,y, label= 'Loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Intresto ')
plt.legend()
plt.show()
