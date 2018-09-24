import numpy as np
import math
# EXO 4.3
# MC

def f(x):
    return 3*x**2 + 2*x - 1 + np.sin(2*math.pi*x)

def montecarlo(f, a, b, N):

    x= a + (b-a)*np.random.rand(N)
    J_N = 0
    V_N = 0
    for xi in x:
        J_N += (b-a)/N*f(xi)
    
    for xi in x:
        V_N += (b-a)/(N-1)*(f(xi)-J_N)**2
    V_N = np.var(x)
#print(J_N, V_N)
    return J_N, V_N

def allstats(f,a,b,Nmax,k):
    fv = np.vectorize(f)
    # calcule un tableau de taille Nmax x nb de f(v) pour v dans [a,b]
    x = fv(a + (b-a)*np.random.random((Nmax, k)))
    # calcule les sommes cumulées divisées par 1/N pour chaque colonne
    y = 1/np.arange(1, Nmax+1)[:, None] * np.cumsum(x, axis=0)
    # calcule les moyennes sur chaque colonne
    mean = np.mean(y, axis=1)
    # calcule les variances sur chaque colonnes
    var = np.var(y, axis=1)
    return (mean,var)

#Nmax = 10000; k = 1000;
## valeurs de N
#N = np.arange(1,Nmax+1)
import matplotlib.pyplot as plt

#mean,var = allstats(f,0,1,Nmax,k)
## figure
#plt.figure(figsize=(8,5))
#plt.title(r"Convergence de la méthode de Monte-Carlo sur $k = {k}$ évaluations")
#plt.plot(np.abs(mean-1), label=r"$10E_N \times N^{1/2}$")
#plt.plot(var, label=r"$\mathrm{Var}(J_N) \times N$")
#plt.xlabel(r"$N$")
#plt.legend()
#ax = plt.gca()
#ax.set_xscale('log')
#ax.set_yscale('log')

#plt.show()
a=0.0
b=1.0
N = 11
print("Approx int(f) ", montecarlo(f, a, b, N))

N_0 = 101
x_0 = np.linspace(a,b,N_0)
x = np.linspace(a,b,N)
y = f(x_0)


if True:
    liste = np.array([2**i for i in range(1, 15)])
    data_0, data_1 = np.vectorize(lambda N: montecarlo(f,a,b,N))(liste)
    OneOver_N = np.vectorize(lambda N: 1.0/N)(liste)
    OneOver_SQRT_N = np.vectorize(lambda N: 1.0/math.sqrt(N))(liste)
    OneOver_N2 = np.vectorize(lambda N: 1.0/N**2)(liste)
    
    plt.figure(figsize=(8,5))
    plt.title("Convergence linéaire de la méthode des montecarlo")
    plt.xlabel(r"$N$")
    plt.ylabel(r"$N \times E_N$")
    #plt.ylim(0,3)
    ax = plt.gca()
    ax.set_xscale('log')
    ax.set_yscale('log')
    plt.plot(liste, OneOver_SQRT_N, label=r"1/sqrt(N)")
    plt.plot(liste, OneOver_N, label=r"1/N")
    plt.plot(liste, OneOver_N2, label=r"1/N**2")
    plt.plot(liste, np.abs(1-data_0), label=r"Methode montecarlo Esp")
    plt.plot(liste, np.abs(data_1), label=r"Methode montecarlo Var")
    
    plt.legend()
    plt.show()

