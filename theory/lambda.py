print((lambda a, b : a+b)(3,7))

# lambda 후, 들어갈 매개변수들, : 후 계산될 수식으로 함수를 정의할 수 있다.


# 자주 나오는 lambda 사용예시 1
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
# 위 배열을 점수 순으로 정렬하라

print(lambda x:x[1])

print(sorted(array, key=lambda x:x[1]))


# 자주 나오는 lambda 사용예시 2
list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b : a+b, list1, list2)
print(list(result))