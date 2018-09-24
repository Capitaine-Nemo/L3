import numpy as np
import math
# EXO 4.1
# Rectangle

# x 0, 1=> 1/2
def f(x):
    return 3*x**2 + 2*x - 1 + np.sin(2*math.pi*x)

    #return x

def rectangle(f, a, b, N, alpha):
    x= np.linspace(a,b, N)
    #print(x)
    integral = 0.0
    h = (b-a)/(N-1)
    #print("h", h)
    for n in range(N-1):
        x_n = (n+alpha) * h
        
        #print(x_n)
        #integral += h*(alpha*f(x_n)+(1.0-alpha)*f(x_n_p_one))
        integral += h*f(x_n)
    return integral

def rectangles(f,a,b,N, alpha=0.5):
    delta = (b-a)/N
    J = 0
    for i in range(N):
        x = a + delta*(i+alpha)
        J += f(x)*delta
    return J

a=0.0
b=1.0
N = 11
alpha = [0., 0.5, 1.0]
for a_0 in alpha:
    print("Approx int(f) alpha=: ", a_0, rectangle(f, a, b, N, a_0))

import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
from matplotlib.collections import PatchCollection
alpha=0.5

N_0 = 101
x_0 = np.linspace(a,b,N_0)
x = np.linspace(a,b,N)
#y = np.sqrt(1-x**2)
y = f(x_0)
#print x
#print y
plt.figure()
dx=x[1]-x[0]
#circle= pylab.Circle((0, 0), 1)
#circle= Wedge((0, 0), 1, 0, 180, fill = False)
plt.plot(x_0, y, "k")
patches=[]
#patches.append(circle)
#plt.gca().add_patch(circle)
for i in range(len(x)-1):
    rect= plt.Rectangle((x[i], 0), dx, f((i+alpha) * dx), fc='b', ec='k')
    rect.set_alpha(0.5)
    plt.gca().add_patch(rect)
#patches.append(rect)


plt.title('Methode des rectangles')
plt.xlim(a,b)
plt.xticks(np.arange(a, b+0.001, step=dx))
#plt.savefig('area')
plt.show()
if True:
    liste = np.array([2**i for i in range(1, 20)])
    data_0 = np.vectorize(lambda N: rectangle(f,a,b,N,0))(liste)
    data_05 = np.vectorize(lambda N: rectangle(f,a,b,N,0.5))(liste)
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
    plt.plot(liste, np.abs(1-data_0), label=r"Methode rectangle alpha = 0")
    plt.plot(liste, np.abs(1-data_05), label=r"Methode rectangle alpha = 0.5")
    plt.legend()
    plt.show()
if False:
    # liste des valeurs de N
    liste = np.arange(10,1000)
    # applique la fonction sur chaque élément de la liste
    data = np.vectorize(lambda N: rectangles(f,a,b,N,0.5))(liste)
    plt.figure(figsize=(8,5))
    plt.title("Convergence linéaire de la méthode des rectangles")
    plt.xlabel(r"$N$")
    plt.ylabel(r"$N \times E_N$")
    #plt.ylim(0,3)
    plt.plot(liste, np.abs(1-data)*liste**2)
    plt.show()
