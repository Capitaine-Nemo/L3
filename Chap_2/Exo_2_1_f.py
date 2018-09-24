
def Exo_F(n):
    u_0=1
    v_0=1
    for i in range(n):
        
        u_1 = u_0 + v_0
        v_1 = 2*u_0 - v_0
        u_0, v_0 = u_1, v_1
    return u_0, v_0

n = 100

print("n=",n ,"Exo_F",  Exo_F(n))       


