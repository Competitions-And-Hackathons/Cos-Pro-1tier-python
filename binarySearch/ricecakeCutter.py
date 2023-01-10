input1 = input()
N = int(input1.split(" ")[0])
M = int(input1.split(" ")[1])

rice_cakes = list()

input2 = input()
for cake_input in input2.split(" "):
    rice_cakes.append(int(cake_input))

answer = 0

for H in reversed(range(max(rice_cakes))):
    rice_length = 0
    for rice_cake in rice_cakes:
        rice_length += max(rice_cake-H, 0)
    
    if rice_length == M:
        answer = H
        break

print(answer)