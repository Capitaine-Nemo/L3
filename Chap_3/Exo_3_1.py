import numpy as np

array5 = np.array([[1.1,2.2,3.3,4.4],[1,2,3,4]]) # matrice de taille 2x4 de flottants

for i in array5:
    # line by line
    print(i)    
    print(np.sum(i))

print(np.arange(5, 10))
print(np.arange(3, 10, 2))

print(np.linspace(2, 5, 10))


# a = np.array([[1,2,3], [4,5,6]])
# np.reshape(a, 6)
# np.reshape(a, 6, order='F')

a = np.arange(1, 7)
b= np.reshape(a, (3,2))
print(np.reshape(a, (3,2)))
# print(b[0][0])  #equiv print(b[0,0])
#print(b)
print(np.reshape(a, (3,2)))
print(np.reshape(a, (2,3)))
print(np.reshape(a, (3,2), order='F'))
