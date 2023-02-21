parsed_input = input().split()
M = int(parsed_input[0])
N = int(parsed_input[1])

table = list()
for _ in range(M):
    table.append(input())

MBTI_count = 0

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]

for y in range(M):
    for x in range(N):
        first_letter = table[y][x]
        if first_letter == 'E' or first_letter == 'I':
            for dir in range(8):
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0 <= nx and nx < N and 0 <= ny and ny < M :
                    second_letter = table[ny][nx]
                    if second_letter == 'N' or second_letter == 'S':

                        nx = nx + dx[dir]
                        ny = ny + dy[dir]

                        #print(first_letter + second_letter)

                        if 0 <= nx and nx < N and 0 <= ny and ny < M :
                            third_letter = table[ny][nx]
                            if third_letter == 'F' or third_letter == 'T':
                                nx = nx + dx[dir]
                                ny = ny + dy[dir]

                                #print(first_letter + second_letter + third_letter)

                                if 0 <= nx and nx < N and 0 <= ny and ny < M :
                                    last_letter = table[ny][nx]
                                    if last_letter == 'P' or last_letter == 'J':
                                        MBTI_count += 1
                                        #print(first_letter + second_letter + third_letter + last_letter)

print(MBTI_count)