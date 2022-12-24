position = input()

x = 0 
for x_index, x_input in enumerate("abcdefgh"):
    if x_input == position[0]:
        x = x_index + 1
        break

y = int(position[1])

x_delete = 0
y_delete = 0

if x == 1 or x == 8:
    x_delete = -2
elif x == 2 or x == 7:
    x_delete = -1

if y == 1 or y == 8:
    y_delete = -2
elif y == 2 or y == 7:
    y_delete = -1

position_count = 8

if x_delete + y_delete == -4:
    position_count = 2

elif x_delete + y_delete == -3:
    position_count = 3

elif x_delete + y_delete == -2:
    position_count = 4

elif x_delete + y_delete == -1:
    position_count = 6

print(position_count)