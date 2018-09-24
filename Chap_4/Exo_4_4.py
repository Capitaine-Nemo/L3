import numpy as np
import math
# EXO 4.4

#import sympy as sp
#sp.init_printing()
## défini les symboles
#func = sp.Function("f")
#x = sp.Symbol("x")
#xn = sp.Symbol("x_{n}")
#xp = sp.Symbol("x_{n+1}")
#m = (xn+xp)/2
## définit le polynôme
#pn = (x-m)*(x-xp)/(xn-m)/(xn-xp)*func(xn) + (x-xn)*(x-xp)/(m-xn)/(m-xp)*func(m) + (x-xn)*(x-m)/(xp-xn)/(xp-m)*func(xp)
## calcule et simplifie l'intégrale
#integral = sp.simplify(sp.integrate(pn,(x,xn,xp)))
#print(integral)
#print(sp.simplify(integral.subs(xp,xn+sp.Symbol("\delta"))))


def f(x):
    return 5*x**4+ 4*x**3+ 3*x**2 + 2*x - 3 + 4*np.sin(8*math.pi*x)

def rectangles(f,a,b,N, alpha=0.5):
    delta = (b-a)/N
    J = 0
    for i in range(N):
        x = a + delta*(i+alpha)
        J += f(x)*delta
    return J

def trapezes(f, a, b, N):
    
    x= np.linspace(a,b, N)
    
    h = (b-a)/(N-1)
    integral = 0.5*h*(f(a)+ f(b))
    for n in range(1, N-1):
        integral += h*f(n * h)
    return integral

def simpson(f,a,b,N):
    delta = (b-a)/N
    J = delta/6*(f(b)-f(a))
    for i in range(0,N):
        x = a + delta*i
        J += delta/3*f(x) + 2*delta/3*f(x+delta/2)
    return J


a = 0.0
b = 1.0
N = 11
print("Approx int(f) ", trapezes(f, a, b, N))

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection

N_0 = 101
x_0 = np.linspace(a,b,N_0)
x = np.linspace(a,b,N)
y = f(x_0)
plt.plot(x_0, y)

liste = np.array([i for i in range(2, 10)])

data_rectangles = np.vectorize(lambda N: rectangles(f,a,b,N))(liste)
data_trapezes = np.vectorize(lambda N: trapezes(f,a,b,N))(liste)
data_simpson = np.vectorize(lambda N: simpson(f,a,b,N))(liste)
OneOver_N = np.vectorize(lambda N: 1.0/N)(liste)
OneOver_N2 = np.vectorize(lambda N: 1.0/N**2)(liste)
OneOver_N3 = np.vectorize(lambda N: 1.0/N**3)(liste)

plt.figure(figsize=(8,5))
plt.title("Convergences de différentes méthodes d'intégration")

plt.xlabel(r"$N$")
plt.ylabel(r"$E_N$")
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.plot(liste, OneOver_N, label=r"1/N")
plt.plot(liste, OneOver_N2, label=r"1/N**2")
plt.plot(liste, OneOver_N3, label=r"1/N**3")
plt.plot(liste, np.abs(1-data_rectangles), label=r"Methode rectangles")
plt.plot(liste, np.abs(1-data_trapezes), label=r"Methode trapezes")
plt.plot(liste, np.abs(1-data_simpson), label=r"Methode Simpson")

plt.legend()
plt.show()
