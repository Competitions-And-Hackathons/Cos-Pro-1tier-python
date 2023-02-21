N = int(input())

original_paper = list()

for _ in range(N):
    paper_row = input().split()
    paper_row_int = list()

    for pr in paper_row:
        paper_row_int.append(int(pr))

    original_paper.append(paper_row_int)

white_count = 0
black_count = 0

stack = list([((0, 0), N)])

while stack:
    element = stack.pop()
    
    coordinate = element[0]
    x = coordinate[0]
    y = coordinate[1]
    size = element[1]

    total_sum = 0
    paper = list()
    for y_index in range(y, y+size):
        paper.append(original_paper[y_index][x:x+size])
        total_sum += sum(original_paper[y_index][x:x+size])

    maximum_blue_number = size * size

    if total_sum == 0:
        white_count += 1

    elif total_sum == maximum_blue_number:
        black_count += 1

    else:
        new_size = size//2
        stack.append(((x, y), new_size))

        is_valid_x = 0 <= x + new_size and x + new_size < N
        is_valid_y = 0 <= y + new_size and y + new_size < N

        if is_valid_x:
            stack.append(((x + new_size, y), new_size))

        if is_valid_y:
            stack.append(((x, y + new_size), new_size))

        if is_valid_x and is_valid_y:
            stack.append(((x + new_size, y + new_size), new_size))

        #print(stack)

print(white_count)
print(black_count)

    
    