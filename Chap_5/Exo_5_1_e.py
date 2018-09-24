import numpy as np

def append_to(element, to=[]):
    print(id(to))
#    to.append(element)
#    to = to +[element] # cree une nouvelle liste
    to+=[element]
    print(id(to))
    
    return to

append_to(1)
print("")
append_to(2)
print("")
append_to(2,[])

def isPath(graph, start, end, path):
    print('\nCall of isPath with:',graph, start, end, path)
    if graph is None:
        return False, None
    if start == end:
        path.append(end)
        return True, path
    elif start not in graph:
        return False, None
    else:
        path.append(start)
        #print("graph", graph, "path", path)
        for neighbour in graph[start]:
            if neighbour not in path:
                b, path = isPath(graph, neighbour, end, path)
                if b:
                    return True, path

graph = {1: {3, 4}, 3: {1, 2}, 4: {1}, 2: {3}}
#print(isPath(graph, 1, 2, []))

graph = {1: {3, 4, 5}, 3: {1, 2}, 4: {1,2}, 2: {3, 4, 5}, 5:{1, 2}}

def getAllPath(graph, start, end):
    AllPath = []
    print('\nCall of getAllPath with:',graph, start, end)
    if graph is None:
        return False, None
    if start == end:
        return True, [start, end]
    elif start not in graph:
        return False, None
    else:
        path = []
        path.append(start)
        print("graph", graph, "path", path)
        for neighbour in graph[start]:
            b, path = isPath(graph, neighbour, end, path)
            if b:
                AllPath.append(path)
        return True, AllPath

print(getAllPath(graph, 1, 2))
