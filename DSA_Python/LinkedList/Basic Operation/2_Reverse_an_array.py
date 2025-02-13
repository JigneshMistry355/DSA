import array as arr

def ReverseArray(a,start,end):
    while start < end:
        a[start], a[end] = a[end], a[start]
        start += 1
        end -= 1
    return a

if __name__ == '__main__':
    a = arr.array('i',[20,60,45,75,10,50])
    l = len(a)
    print(f'This is the original list\n  {a}')
    ReverseArray(a,0,l-1)
    print(f'\nThis is the reversed string\n {a}' )

