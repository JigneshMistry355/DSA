arr = [1, 2, 3, 4]
x = 0


if x in arr:
    print(arr.index(x))
    print(arr.index(x,1,3)) # between index 1 and 3
else:
    print(-1)

