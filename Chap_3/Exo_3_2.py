import numpy as np
import matplotlib.pyplot as plt
import timeit

def diff_list(v, h):
    d_v = list(range(len(v)-1))
    for i in range(len(v)-1):
        d_v[i] = (v[i+1]-v[i])/h
    return d_v

def diff_np(v, h):
    n = v.size
    d_v = 1/h*(v[1:n] - v[0:n-1])
    return d_v

x = np.linspace(0, 2*np.pi, 1000)
y = np.cos(x)
l_y= list(y)
#d_l_y = diff_list(l_y, x[1]-x[0])
#d_y = diff_np(y, x[1]-x[0])

setup_l = '''
import numpy as np
import matplotlib.pyplot as plt
import timeit
def diff_list(v, h):
    d_v = list(range(len(v)-1))
    for i in range(len(v)-1):
        d_v[i] = (v[i+1]-v[i])
    return d_v

x = np.linspace(0, 2*np.pi, 1000)
y = np.cos(x)
l_y= list(y)
'''

setup = '''
import numpy as np
import matplotlib.pyplot as plt
import timeit

def diff_np(v, h):
    n = v.size
    d_v = (v[1:n] - v[0:n-1])
    return d_v

x = np.linspace(0, 2*np.pi, 1000)
y = np.cos(x)
l_y= list(y)
'''
nb = 10000  # 10000
t_l = min(timeit.Timer('diff_list(l_y, x[1]-x[0])', setup=setup_l).repeat(10, nb))
t_np = min(timeit.Timer('diff_np(y, x[1]-x[0])', setup=setup).repeat(10, nb))
print("np est ",t_l/t_np,"plus rapide")
#timeit.timeit('diff_list(l_y, x[1]-x[0])', number=10000)
#timeit.timeit('diff_np(y, x[1]-x[0])', number=10000)
#print(d_l_y[0], d_y[0])
#x_d = np.linspace(0, 2*np.pi, 99)
#d_l_y_np = np.array(d_l_y)
#z = -np.sin(x)
#plt.plot(x, y)
#plt.plot(x, z)
#plt.plot(x_d, d_l_y_np)

#plt.show()


