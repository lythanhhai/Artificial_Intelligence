graph = {
    'a': [],
    'b': [],
    'c': [],
    'd': [],
    'e': [],
    'f': []
}
def addEdge(u, v):
    graph[u].append(v)
  
def printAllPathsUtil(u, d, visited, path):
    visited[u]= True
    path.append(u)

    if u == d:
        print (path)
    else:
        for i in graph[u]:
            if visited[i]== False:
                printAllPathsUtil(i, d, visited, path)

        path.pop()
        visited[u]= False
  
  
def printAllPaths(s, d, numberEdge):
    visited = [False] * (numberEdge)
    path = []
    printAllPathsUtil(s, d, visited, path)  

#graph = ["a", "b", "c", "d", "e", "f"]
numberEdge = 7
for i in range(0, numberEdge):
    a, b = map(str, input().split(", "))
    addEdge(a, b)

print(graph)
print("Nhập nguồn: ")
s = input()
print("Nhập đích: ")
d = input()
print(f"Tất cả các đường từ ${s} đến ${d}: ")
printAllPaths(s, d, numberEdge)