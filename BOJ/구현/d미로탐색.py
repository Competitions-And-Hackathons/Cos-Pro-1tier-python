from collections import deque

def bfs(x, y):
    q = deque([(x, y, 0)])
    visited[x][y] = True
    while q:
        x, y, d = q.popleft()
        if x == N - 1 and y == M - 1:
            return d
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))
    return -1

N, M = 4, 6
maze = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]
visited = [[False] * M for _ in range(N)]

print(bfs(0, 0) + 1)