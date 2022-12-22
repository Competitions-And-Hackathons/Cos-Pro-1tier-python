numberString = input()

result = int(numberString[0])
numberString = numberString[1:]

for number in numberString:
    plus = result + int(number)
    multiply = result * int(number)

    if plus > multiply :
        result = plus
    else:
        result = multiply

print(result)