# itertools
# heapq
# bisect
# collections
# maths

# 기본 라이브러리
data = [1,2,3,4,5]

# sum()
print(sum(data))

# min, max
print(min(data), max(data))


# eval : 문자열로 쓰인 수식을 숫자로 계산한 결과를 보여줌
result = eval("(3+5)*7")
print(result)


# sorted : 정렬 함수, 기본적으로 오름차순이다.
result = sorted([9,1,8,5,4])
print(result)

result = sorted([9,1,8,5,4], reverse=True)
print(result)


array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key = lambda x : x[1], reverse=True)
print(result)



# 순열과 조합
# 순열 : nPk, 조합 : nCk


from itertools import permutations, combinations
data = ['A', 'B', 'C']

result = list(permutations(data, 2))
print("nPk", list(result))

result = list(combinations(data, 2))
print("nCk",list(result))

# 중복 순열, 중복 조합도 구현 가능하다.
from itertools import product, combinations_with_replacement
result = list(product(data, repeat=3))
print("중복 nPk", list(result))

result = list(combinations_with_replacement(data, 2))
print("중복 nCk",list(result))


# 등장 횟수를 세는 Counter도 있다.
from collections import Counter
counter_info = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter_info['red'])
print(dict(counter_info))

# 최대공약수(gcd), 최소공배수(lcm)를 구하는 방법
import math
def lcm(a, b):
    return a*b/math.gcd(a,b)

a = 21
b = 14

print(math.lcm(a, b))
print(math.gcd(a, b))