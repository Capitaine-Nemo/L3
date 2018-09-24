import matplotlib.pyplot as plt
import matplotlib
#matplotlib.axes.Axes.imshow
#matplotlib.pyplot.imshow
import numpy as np


np.random.seed(19680801)
A = np.random.rand(10,10)
plt.figure(figsize=(6,5))
plt.imshow(A, vmin=0, vmax=1)
plt.colorbar()
print(A.shape)
plt.xticks(range(A.shape[0]))
plt.yticks(range(A.shape[1]))
plt.show()
