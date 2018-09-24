import numpy as np
import math
# EXO 4.2
# trapezes

# x 0, 1=> 1/2
def f(x):
    return 3*x**2 + 2*x - 1 + np.sin(2*math.pi*x)

    #return x

def trapezes(f, a, b, N):

    x= np.linspace(a,b, N)
    
    h = (b-a)/(N-1)
    integral = 0.5*h*(f(a)+ f(b))
    for n in range(1, N-1):
        integral += h*f(n * h)
    return integral

a=0.0
b=1.0
N = 11
print("Approx int(f) ", trapezes(f, a, b, N))

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection

N_0 = 101
x_0 = np.linspace(a,b,N_0)
x = np.linspace(a,b,N)
y = f(x_0)

if True:
    liste = np.array([2**i for i in range(1, 20)])
    data_0 = np.vectorize(lambda N: trapezes(f,a,b,N))(liste)
    OneOver_N = np.vectorize(lambda N: 1.0/N)(liste)
    OneOver_N2 = np.vectorize(lambda N: 1.0/N**2)(liste)
    
    plt.figure(figsize=(8,5))
    plt.title("Convergence linéaire de la méthode des rectangles")
    plt.xlabel(r"$N$")
    plt.ylabel(r"$N \times E_N$")
    #plt.ylim(0,3)
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.plot(liste, OneOver_N, label=r"1/N")
    plt.plot(liste, OneOver_N2, label=r"1/N**2")
    plt.plot(liste, np.abs(1-data_0), label=r"Methode trapezes")
    
    plt.legend()
    plt.show()

