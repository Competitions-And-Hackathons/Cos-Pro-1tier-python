number1 = int(input())
number2 = input()

for i in reversed(range(3)) :
    print(number1 * int(number2[i]))

print(number1 * int(number2))