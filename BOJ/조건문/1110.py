number = int(input())
original_number = number
a = number//10
b = number%10

cycle_num = 0

while True:
    cycle_num += 1

    sum = a+b
    new_number = b*10 + sum%10

    if new_number == original_number:
        break

    a = new_number//10
    b = new_number%10

print(cycle_num)
