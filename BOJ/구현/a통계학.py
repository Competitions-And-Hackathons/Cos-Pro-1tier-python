n = int(input())
input_list = list()

for _ in range(n):
    input_list.append(int(input()))

input_list.sort()

# 1. 산술 평균
print(round(sum(input_list)/n))

# 2. 중앙값
print(input_list[n//2])

# 3. 최빈값
from collections import Counter
counter_example = Counter(input_list)
counter_example = counter_example.most_common()

maximum_appear = counter_example[0][1]

counter_example = [i for i in counter_example if i[1] == maximum_appear]
counter_example.sort(key= lambda x : x[0])

#print(counter_example)

if len(counter_example) > 1:
    print(counter_example[1][0])

else:
    print(counter_example[0][0])

# 4. 범위 출력
print(max(input_list) - min(input_list))