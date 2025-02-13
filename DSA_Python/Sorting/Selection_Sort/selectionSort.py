import array as arr

a = arr.array('i',[64,22,45,12,11])

for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[min] > a[j]:
            min = j
    if i != min:
        a[i], a[min] = a[min], a[i]

print(list(a))