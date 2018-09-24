
def Exo_G(n_0, K):
    v_0 = n_0
    v_n = []
    for k in range(K): 
        if v_0%2==0:
            v_k = v_0//2
        else:
            v_k = 3*v_0 + 1
        v_0 = v_k
        v_n.append(v_0)
    return v_n[-5:]

n = 10
K = 1000

print("n=",n ,"K=", K,"Exo_G",  Exo_G(n, K))       
n = 100

print("n=",n ,"K=", K,"Exo_G",  Exo_G(n, K))       
n = 1000

print("n=",n ,"K=", K,"Exo_G",  Exo_G(n, K))       
n = 10000

print("n=",n ,"K=", K,"Exo_G",  Exo_G(n, K))       

lst = 100
l = [1, 2, 3]
t = tuple(l[i] if i != len(l)-1 else lst for i in range(len(l)) )
print(l, t)
