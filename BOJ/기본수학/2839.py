sugarPowders = int(input())
originalSugarPodwers = sugarPowders

fiveKgs = sugarPowders//5


for fiveIdx in reversed(range(fiveKgs + 1)):
    sugarPowders = originalSugarPodwers
    sugarPowders -= fiveIdx*5

    threeKgs = sugarPowders//3
    sugarPowders -= threeKgs*3

    if sugarPowders == 0:
        print(fiveIdx + threeKgs)
        exit()

print(-1)
