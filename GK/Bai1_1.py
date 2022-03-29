
def initialTop(numberTop):
    Tops = []
    for i in range(0, numberTop):
        Tops.append(input())
    return Tops

def initialEdge(numberEdge):
    Edges = []
    for i in range(0, numberEdge):
        edge1, edge2 = map(str, input().split(", "))
        Edges.append((edge1, edge2))
    return Edges

# bắt đầu khởi tạo tập đỉnh và tập cạnh để biểu diễn đồ thị
numberTop = int(input()) # số đỉnh V
numberEdge = int(input()) # số cạnh E
print("Các đỉnh là: ", initialTop(numberTop))

print("Các cạnh là: ", initialEdge(numberEdge))


