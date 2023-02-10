input_S = input()
input_S = input()

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0

max_x = 0
min_x = 0
max_y = 0
min_y = 0

x=0
y=0


walk_history = set([(0, 0)])


for s in input_S:
    if s == 'F':
        x += dx[dir]
        y += dy[dir]

        walk_history.add((x, y))

        max_x = max(max_x, x)
        min_x = min(min_x, x)
        max_y = max(max_y, y)
        min_y = min(min_y, y)

    elif s == 'L':
        dir = (dir+1) % 4

    elif s == 'R':
        dir = (dir+3) % 4


m = max_x - min_x + 1
n = max_y - min_y + 1

maze = [['#'] * m for _ in range(n)]

for walk_element in list(walk_history):
    walk_x = walk_element[0] + min_x * (-1)
    walk_y = walk_element[1] + min_y * (-1)

    maze[walk_y][walk_x] = '.'


for maze_row in maze:
    print(''.join(maze_row))