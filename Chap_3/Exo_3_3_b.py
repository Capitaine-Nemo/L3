"""
============
Layer Images
============

Layer images above one another using alpha blending
"""
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as colors


x = np.arange(0, 10)
y = np.arange(0, 10)
X, Y = np.meshgrid(x, y)

# when layering multiple images, the images need to have the same
# extent.  This does not mean they need to have the same shape, but
# they both need to render to the same coordinate system determined by
# xmin, xmax, ymin, ymax.  Note if you use different interpolations
# for the images their apparent extent could be different due to
# interpolation edge effects
#plt.figure(figsize=(9,5)) # taille de la figure (en inches)

extent = np.min(x), np.max(x), np.min(y), np.max(y)

fig = plt.figure(figsize=(6,5))

np.random.seed(19680801)
Z1 = np.random.rand(10,10)
#im1 = plt.imshow(Z1, cmap="viridis", interpolation='none', extent=extent, norm=colors.Normalize(vmin=0.0, vmax=1.0))
im1 = plt.imshow(Z1, vmin=0, vmax=1)

#ca = plt.gca()
#ylim = ca.get_ylim()
#ca.set_ylim(ylim[::-1])
#ca.set_title("Origin from rc, reversed y-axis")

#divider = make_axes_locatable(plt.gca())
#cax = divider.append_axes("right", "5%", pad="3%")
#plt.colorbar(im1, cax=cax, extend="neither")#,ticks=[0.0,0.3, 0.4, 0.6, 0.8, 1.0])

#plt.savefig("test", dpi=100) # exporte la figure en PNG
#
#plt.tight_layout()
plt.xticks(range(Z1.shape[0]))
plt.yticks(range(Z1.shape[1]))
plt.colorbar()
plt.show()
