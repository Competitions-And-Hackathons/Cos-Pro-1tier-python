## 순열
print("순열, permutations")

from itertools import permutations

for i in permutations([1,2,3,4], 2):
    print(i, end=" ")

#-----------------------------------------#

## 조합
print("\n\n조합, combinations")
from itertools import combinations

for i in combinations([1,2,3,4], 2):
    print(i, end=" ")

#-----------------------------------------#

## 중복순열
print("\n\n중복순열, product")
from itertools import product

for i in product(range(3), range(3), range(3)):
    print(i, end=" ")

#-----------------------------------------#

## 중복조합
print("\n\n중복조합, combinations_with_replacement")
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")
