"""
=============
Contour Image
=============

Test combinations of contouring, filled contouring, and image plotting.
For contour labelling, see also the :doc:`contour demo example
</gallery/images_contours_and_fields/contour_demo>`.

The emphasis in this demo is on showing how to make contours register
correctly on images, and on how to get both of them oriented as desired.
In particular, note the usage of the :doc:`"origin" and "extent"
</tutorials/intermediate/imshow_extent>` keyword arguments to imshow and
contour.
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Default delta is large because that makes it fast, and it illustrates
# the correct registration between image and contours.
delta = 0.1

extent = (-3, 3, -3, 3)

x = np.linspace(-3.0, 3.00, 100)
y = np.linspace(-3.0, 3.00, 100)
X, Y = np.meshgrid(x, y)
Z1 = -Y/5.0
Z2 = np.exp(-X**2 - Y**2)
Z = Z1 + Z2

# Boost the upper limit to avoid truncation errors.
levels = np.arange(-0.6, 1.5 , 0.005)

#norm = cm.colors.Normalize(vmax=abs(Z).max(), vmin=-abs(Z).max())
#cmap = cm.PRGn
fig = plt.figure(figsize=(12,5))
fig.suptitle(r'Représentation de $\frac{-y}{5} + e^{-x^2-y^2}$')

sub = fig.add_subplot(1,2,1)
#_axs = sub.gca()
# fig, _axs = plt.subplots(nrows=1, ncols=2)
# fig.subplots_adjust(hspace=0.3)
#axs = _axs.flatten()

cset1 = sub.contourf(X, Y, Z,
                        levels,
                        #norm=norm,
                        #cmap=cm.get_cmap(cmap, len(levels) - 1)
                        extent=extent,
                         vmin= -0.50,
                         vmax=  1.00
                        )

sub.set_title('Densité')
cbar = fig.colorbar(cset1, ax=sub)
cbar.set_ticks(np.linspace(-0.5,1.0,7))

sub = fig.add_subplot(1,2,2)
#axs[1].imshow(Z, extent=extent, cmap=cmap, norm=norm)
cset4 = sub.contour(X, Y, Z, levels=np.linspace(-0.5,1,13), extent=extent)
sub.set_title("Contours")
sub.set_aspect('equal')
cbar =fig.colorbar(cset4, ax=sub)
cbar.set_ticks(np.linspace(-0.5,1.0,7))

fig.tight_layout()
plt.show()

