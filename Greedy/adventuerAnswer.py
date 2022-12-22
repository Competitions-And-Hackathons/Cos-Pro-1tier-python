N = int(input())
fearRates = list(map(int, input().split()))

groupNumber = 0
memberCount = 0
fearRates = sorted(fearRates)

for fear in fearRates:
    memberCount += 1
    if memberCount >= fear:
        groupNumber += 1
        memberCount = 0

print(groupNumber)