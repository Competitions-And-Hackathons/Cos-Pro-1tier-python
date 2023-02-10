from collections import Counter

counter_example = Counter([1, 3, 8, -2, 2])
counter_example = counter_example.most_common()
counter_example.sort(key= lambda x : x[0])

print(counter_example)

if len(counter_example) > 1:
    print(counter_example[1][0])

else:
    print(counter_example[0][0])