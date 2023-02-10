def solve_maze(n, instructions):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = dir = 0
    grid = [[0] * 100 for i in range(100)]

    
    for i in range(n):
        if instructions[i] == 'F':
            x += dx[dir]
            y += dy[dir]
            grid[x][y] = 1
        elif instructions[i] == 'L':
            dir = (dir + 1) % 4
        elif instructions[i] == 'R':
            dir = (dir + 3) % 4
    left = top = bottom = right = 0

    for i in range(100):
        for j in range(100):
            if grid[i][j] == 1:
                left = min(left, j)
                right = max(right, j)
                top = min(top, i)
                bottom = max(bottom, i)

    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if grid[i][j] == 1:
                print(".", end="")
            else:
                print("#", end="")
        print("")

if __name__ == "__main__":
    n = int(input().strip())
    instructions = input().strip()
    solve_maze(n, instructions)
