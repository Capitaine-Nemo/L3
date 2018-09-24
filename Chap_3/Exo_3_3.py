import numpy as np
import matplotlib.pyplot as plt


#x = np.linspace(0,1,50)
#y = x**2

#plt.figure(figsize=(8,5)) # taille de la figure (en inches)
#plt.title(r'Graphique de $x^2$') # titre de la figure (du code LaTeX peut être inclus)
#plt.xlabel(r'$x$') # titre de l'axe horizontal
#plt.ylabel(r'$y$') # titre de l'axe vertical
#plt.plot(x, y, marker='o', label=r"$x^2$") # légende
#plt.legend() # affiche la légende
#plt.savefig("test.pdf") # exporte la figure en PDF
#plt.savefig("test", dpi=100) # exporte la figure en PNG
#plt.show()

x = np.linspace(0,2*np.pi, 100)
y_cos_1 = np.cos(x)
y_cos_2 = np.cos(2*x)
y_cos_3 = np.cos(3*x)

y_sin_1 = np.sin(x)
y_sin_2 = np.sin(2*x)
y_sin_3 = np.sin(3*x)

plt.figure(figsize=(9,5)) # taille de la figure (en inches)
plt.title(r'Graphique de $sin(kx)$') # titre de la figure (du code LaTeX peut être inclus)
plt.xlabel(r'$x$') # titre de l'axe horizontal
plt.ylabel(r'$y$') # titre de l'axe vertical
plt.plot(x, y_sin_1, label=r"$sin(x)$") # légende
plt.plot(x, y_sin_2, label=r"$sin(2x)$") # légende
plt.plot(x, y_sin_3, label=r"$sin(3x)$") # légende
plt.plot(x, y_cos_1, label=r"$cos(x)$") # légende
plt.plot(x, y_cos_2, label=r"$cos(2x)$") # légende
plt.plot(x, y_cos_3, label=r"$cos(3x)$") # légende
plt.xticks(np.arange(0, 2*np.pi+1, step=np.pi/2), ('0', '$\pi/2$', '$\pi$', '3$\pi/2$', '2$\pi$'))
plt.legend() # affiche la légende
#plt.savefig("test.pdf") # exporte la figure en PDF
#plt.savefig("test", dpi=100) # exporte la figure en PNG
plt.show()
