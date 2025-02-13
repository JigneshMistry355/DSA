#  Sequential Seach

import array as arr

def linearSearch(a, b, l):
    for i in range(0, l):
        if a[i] == b:
            return i
    return -1
    
if __name__ == "__main__":
    
    a = arr.array("i",[10,20,30,40,50])
    b = 30
    l = len(a)

    result = linearSearch(a,b,l)
    if result == -1:
        print(f'{b} is not present in the array')
    else:
        print(f'{b} is present in the array')


