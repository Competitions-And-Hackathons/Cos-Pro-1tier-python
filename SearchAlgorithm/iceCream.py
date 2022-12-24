n, m = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)

def search(graph, x, y):
    if x < 0  or y < 0 or x >= n or y>= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        search(graph, x+1, y)
        search(graph, x-1, y)
        search(graph, x, y+1)
        search(graph, x, y-1)

        return True

    else:
        return False

icecreamCount = 0

for x in range(n):
    for y in range(m):
        if search(graph, x, y):
            icecreamCount += 1

print(icecreamCount)
