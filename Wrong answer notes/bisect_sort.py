from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4


leftest_index = bisect_left(a, x)
rightest_index = bisect_right(a, x)
print(rightest_index- leftest_index)
