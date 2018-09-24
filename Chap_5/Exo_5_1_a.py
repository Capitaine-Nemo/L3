import numpy as np
def complet(n):
    return {i:{a for a in range(n)}-set([i]) for i in range(n)}
print(complet(4))
print(complet(5))

def petersen():
    s = dict()
    for i in range(5):
        s[i] = set([(i+1)%5, (i+4)%5, i+5])
        s[i+5] = set([(i+2)%5+5, (i+3)%5 +5, i])
    print(s)
                    #return {i:{a for a in range(n)}-set([i]) for i in range(n)}

petersen()

def corriger(graph):
    out =  graph.copy()
    for s in graph:
        
        for a in graph[s]:
            if a in out:
                out[a].add(s)
            else:
                out[a] ={s}
    return out

out = corriger({1:{3,4},3:{2}})
print(out)

def generate_Edges(graph):
    s_E =set()
    for v in graph:
        for i in graph[v]:
            if v<i:
                s_E.add((v,i))
            else:
                s_E.add((i,v))
    return s_E
print(generate_Edges(out))
