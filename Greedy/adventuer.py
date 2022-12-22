N = int(input())
fearRates = list(map(int, input().split()))

groupNumber = 0
fearRates = sorted(fearRates, reverse=True)

while True:
    if len(fearRates) == 0:
        break

    maxFear = max(fearRates)
    del fearRates[0]

    if len(fearRates) >= maxFear - 1:
        groupNumber += 1
        fearRates = fearRates[maxFear-1:]

    else:
        break

print(groupNumber)