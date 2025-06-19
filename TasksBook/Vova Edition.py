import numpy as np
import matplotlib.pyplot as plt

table = np.array([[0, 0.5, 1, 1.5, 2, 2.5, 3], [0, 0.13, 1, 3.38, 8.00, 15.63, 27]])
np.save('test1.npy', table)
graph = np.load('test1.npy')
x = graph[0]
y = graph[1]
plt.plot(x, y)
plt.xlabel('t, Время')
plt.ylabel('C, c')
plt.show()
