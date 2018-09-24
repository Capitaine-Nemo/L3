import numpy as np

c = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
cond = (c >= 5) # tableau de booléens valant True si >= 5 et False sinon
c[cond] = 5 # assigne la valeur 5 à toutes les entrées de c plus grandes que 5
#print(c)

m = [0.9602, -0.99, 0.2837, 0.9602, 0.7539, -0.1455, -0.99, -0.9111, 0.9602, -0.1455, -0.99, 0.5403, -0.99, 0.9602, 0.2837, -0.99, 0.2837, 0.9602]

m_np = np.array(m)
#print ("size", m_np.size)
cond=(m_np<=0.0)
#print("cond=", cond)
m_np[cond]=0.0
#print(m_np)

m_np = np.array(m)
t=np.arange(2, 3.8, 0.1)
#print(t)
#print ("size", t.size)
#print(np.argmax(m_np))

winner = np.argwhere(m_np == np.amax(m_np))
print(winner)

for w in winner:
    iW = w[0]
    if iW==0:
        print(np.nan, m_np[iW], m_np[iW+1])
    elif iW==m_np.size-1:
        print(m_np[iW-1], m_np[iW], np.nan)
    else:
        print(m_np[iW-1], m_np[iW], m_np[iW+1])
