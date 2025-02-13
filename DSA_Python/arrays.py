import array as arr

a = arr.array('i',[1,2,3])
print("Print the elements of array")
print(a)
print()

print("access element")
print(a[1])
print()

print("Print type of variable")
print(type(a))
print()

print("insert 0 at index 1")
a.insert(1,0)
print()

print("print array after insertion")
print(a)
print()

print("remove 0 from array")
a.remove(0)
print()

print("print array after deletion")
print(a)
