import math, scipy.integrate
import matplotlib.pyplot as plt
import numpy as np

def integrand(t, n, x):
    return math.exp(-x*t)/t**n
def E(n, x):
    return scipy.integrate.quad(integrand, 1, math.inf, args=(n, x))
x = np.linspace(1, 100, 100)
y = np.vectorize(lambda x : integrand(x, 4, 2))(x)
plt.plot(x, y)
ax = plt.gca()
ax.set_yscale('log')
plt.show()


print(E(4,2))
