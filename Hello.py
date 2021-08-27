def func(y):
    return y % 2


print("Hello world");
x = [2, 5, 6, 7, 9, 9, 1, -1]
print(x.count(9))
x.sort()
print(sorted(x))
print(sorted(x, key=func))
