from functools import reduce

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_val = reduce(lambda x, y: x if x > y else y, n)
print(max_val)
