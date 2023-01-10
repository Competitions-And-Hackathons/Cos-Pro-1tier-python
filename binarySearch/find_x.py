from bisect import bisect_left, bisect_right

list = [1, 1, 2, 2, 2, 2, 3]
x = 2

leftest = bisect_left(list, x)
rightest = bisect_right(list, x)

print(rightest - leftest)