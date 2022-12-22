# N원을 500원, 100원, 50월, 10원으로 거슬러 줘야 할 때 최소한의 동전의 갯수를 구하라.

N = input()
N = int(N)

coinNumber = 0

coinTypes = [500, 100, 50, 10]

for coin in coinTypes:
    coinNumber += N//coin
    N %= coin

print(coinNumber)