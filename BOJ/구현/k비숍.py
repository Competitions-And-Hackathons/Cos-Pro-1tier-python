from collections import deque

n = int(input())

"""white_cross_lines = n//2 + n%2
black_cross_lines = n//2 

white_cross_lines_2_number = max(white_cross_lines - 2, 0)
black_cross_lines_2_number = black_cross_lines
if white_cross_lines == black_cross_lines:
    black_cross_lines_2_number -= 1

#print("white_cross_lines_2_number", white_cross_lines_2_number)
#print("black_cross_lines_2_number", black_cross_lines_2_number)

print(white_cross_lines + black_cross_lines + white_cross_lines_2_number + black_cross_lines_2_number)"""

print(n + max(n-2, 0))