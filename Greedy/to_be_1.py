N = input()
N = int(N)

K = input()
K = int(K)

count = 0

while N>1:
    if N%K == 0:
        N //= K
    else: 
        N -=1
    
    count += 1

print(count)