N = int(input())
grades = list(map(int, input().split()))
M = max(grades)
new_avg = 0
for grade in grades:
    new_avg += grade/M*100

new_avg /= N
print(new_avg)