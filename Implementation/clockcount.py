N = int(input())
count = 0

for hour in range(0, N+1):
    for minite in range(0, 60):
        for second in range(0, 60):
            if hour == 3 or hour == 13:
                count += 1
                continue


            miniteString = str(minite)

            if len(miniteString) == 2:
                if miniteString[0] == '3' or miniteString[1] == '3':
                    count += 1
                    continue

            elif len(miniteString) == 1:
                if miniteString[0] == '3':
                    count += 1
                    continue

            
            secondString = str(second)

            if len(secondString) == 2:
                if secondString[0] == '3' or secondString[1] == '3':
                    count += 1
                    continue

            elif len(secondString) == 1:
                if secondString[0] == '3':
                    count += 1
                    continue

print(count)