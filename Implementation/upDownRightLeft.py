N = int(input())
commands = input().split()

x=1
y=1

for command in commands:
    if command == "L":
        nx = x-1

        if nx >= 1:
            x = nx
    
    if command == "R":
        nx = x+1

        if nx <= N:
            x = nx

    if command == "D":
        ny = y+1

        if ny <= N:
            y = ny

    if command == "U":
        ny = y-1

        if ny >= 1:
            y = ny

print(y, x)