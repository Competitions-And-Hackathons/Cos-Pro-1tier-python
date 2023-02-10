inputString = input()
hour = int(inputString.split()[0])
minite = int(inputString.split()[1])

if minite >= 45:
    print(str(hour) + " " + str(minite-45))

else:
    if hour > 0:
        print(str(hour-1) + " " + str(minite+15))
    else:
        print(str(23) + " " + str(minite+15))