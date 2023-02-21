dx = [0, 1, 1]
dy = [1, 1, 0]

parsed_input = input().split()
N = int(parsed_input[0])
M = int(parsed_input[1])

candy_table = [[0] * M for _ in range(N)]


maze = list()
for _ in range(N):
    parsed_maze_row = input().split()
    maze_row = list()
    for r in parsed_maze_row:
        maze_row.append(int(r))

    maze.append(maze_row)

stack = list([((0,0), 0)])

while stack:
    element = stack.pop()
    cordinate = element[0]
    cummulated_candy = element[1]

    
    x = cordinate[0]
    y = cordinate[1]

    current_candy = maze[y][x]
    cummulated_candy += current_candy

    candy_table[y][x] = max(candy_table[y][x], cummulated_candy)


    for dir in range(3):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx and nx < M and 0 <= ny and ny < N:
            stack.append(((nx, ny), cummulated_candy))

print(candy_table[N-1][M-1])