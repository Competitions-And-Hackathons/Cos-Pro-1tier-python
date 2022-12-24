string = input()
string = sorted(string)
print(string)

numberSum = 0
stringConcat = ""
for stringIndex, parsedString in enumerate(string):
    if parsedString.isdigit(): 
        numberSum += int(parsedString)
    else:
        stringConcat += parsedString

print(stringConcat + str(numberSum))
