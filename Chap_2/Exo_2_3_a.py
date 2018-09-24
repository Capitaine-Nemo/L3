
def divisible(n):
    s =set()
    for i in range(100):
        if i%n==0:
            s.add(i)
    return s

n = 2

print("n=",n ,"divisible =>",  divisible(n))       

set_2 = divisible(2)
set_3 = divisible(3)
set_5 = divisible(5)

set_F = (set_3&set_5)-set_2
print("final set => ",set_F)
