import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = [0, 1, 2, 3, 4]
y = [0, 2, 4, 6, 8]

plt.plot(x, y)

plt.title("Our First Graph", fontdict={
          'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('X')
plt.ylabel('Y')

plt.xticks([0, 1, 2, 3, 4])
plt.yticks([0, 2, 4, 6, 8])

plt.show()
