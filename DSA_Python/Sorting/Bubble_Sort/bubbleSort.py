
a = [3,5,1,6,8,7]
size = len(a)

for i in range(size):
    swapped = False
    for j in range(0,size-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            swapped = True
    if swapped == False:
        break

print(a)


            
