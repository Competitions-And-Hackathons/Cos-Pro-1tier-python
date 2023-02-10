inputString = input()
hour = int(inputString.split()[0])
minite = int(inputString.split()[1])

time_consume = int(input())

minite += time_consume

if minite >= 60:
    hour += minite//60
    minite %= 60
    

if hour >= 24:
    hour %= 24

print(str(hour) + " " + str(minite))