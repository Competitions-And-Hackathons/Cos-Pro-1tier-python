from collections import deque

n, m = map(int, input().split())

visited = []
for _ in range(n):
    row = [False] * m
    visited.append(row)

graph = []
for _ in range(n):
    row = list(map(int, input()))
    graph.append(row)


queue = deque()
queue.append((0, 0))

dxys = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]

while len(queue) > 0:
    cordinate = queue.popleft()
    x = cordinate[0]
    y = cordinate[1]
    
    for dxy in dxys:
        ndx = cordinate[0] + dxy[0]
        ndy = cordinate[1] + dxy[1]

        if ndx < 0 or ndx >= n or ndy < 0 or ndy >= m:
            continue

        if graph[ndx][ndy] == 0 or visited[ndx][ndy] == True:
            continue

        if graph[ndx][ndy] == 1 and visited[ndx][ndy] == False:
            graph[ndx][ndy] = graph[x][y] + 1
            queue.append((ndx, ndy))
        
        visited[x][y] = True

#print(graph)
print(graph[n-1][m-1])
