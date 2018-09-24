import numpy as np


# def append_to(element, to=[]):
#     print(id(to))
#     #    to.append(element)
#     #    to = to +[element] # cree une nouvelle liste
#     to += [element]
#     print(id(to))
#
#     return to


# append_to(1)
# print("")
# append_to(2)
# print("")
# append_to(2, [])


def isPath(graph, start, end, path):
    print('\nCall of isPath with:', graph, start, end, path)
    if graph is None:
        return False, None
    if start == end:
        path.append(end)
        return True, path
    elif start not in graph:
        return False, None
    else:
        path.append(start)
        # print("graph", graph, "path", path)
        for neighbour in graph[start]:
            if neighbour not in path:
                b, path = isPath(graph, neighbour, end, path)
                if b:
                    return True, path

def isPath_All(graph, start, end, path, listPath):

    print('\nCall of isPath with:', graph, start, end, path, listPath)
    if graph is None:
        return False, None
    if start == end:
        path.append(end)
        return True, path
    elif start not in graph:
        return False, None
    else:
        path.append(start)

        for neighbour in graph[start]:
            if neighbour not in path:
                b, path = isPath(graph, neighbour, end, path)
                if b:
                    listPath.append(path)
        if listPath:
            return True, listPath
        else:
            return False, []


graph = {1: {3, 4}, 3: {1, 2}, 4: {1}, 2: {3}}
# print(isPath(graph, 1, 2, []))

graph_2 = {1: {3, 4, 5}, 3: {1, 2}, 4: {1, 2}, 2: {3, 4, 5}, 5: {1, 2}}
graph_3 = {1: {3, 4, 5, 6}, 3: {1, 2}, 4: {1, 2}, 2: {3, 4, 5}, 5: {1, 2}, 6:{1}}


def getAllPath(graph, start, end):
    AllPath = []
    print('\nCall of getAllPath with:', graph, start, end)
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
            b, path_2 = isPath(graph, neighbour, end, path.copy())
            if b:
                AllPath.append(path_2)
        return True, AllPath


print(getAllPath(graph, 1, 2))
