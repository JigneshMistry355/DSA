heros=['spider man','thor','hulk','iron man','captain america']

#------------------------xxxxxxxxxxxxxxxxx----------------------------
# Length of the list 
print(f'The length of the list is :: {len(heros)}') # or

def lengthOfList(mylist):
    count = 0
    for i in mylist:
        count += 1
    return count

print(f'The length of the list is :: {lengthOfList(heros)}')

#------------------------xxxxxxxxxxxxxxxxx----------------------------

# Add 'black panther' at the end of this list
item = 'Black Panther'

def myAppend(mylist, item):
    # Append is just concatination of an element to a list
    mylist = mylist + [item]
    return mylist

print(myAppend(heros, item))

def insertAt(mylist,data,index):
    print(f"len of mylist {len(mylist)}")
    if index < 0 or index > lengthOfList(mylist):
        raise Exception()
    if index == len(mylist):
        return myAppend(mylist, data)
    
    # shifting each element from its index to its next index
    # Eg. shifting --hulk from --index 2 to --index 3
    # Likewise shifting all elements including --hulk to --captain america, 
    # one position ahead of its original position
    mylist[index+1:] = mylist[index:]
    mylist[index] = data
    return mylist

print(insertAt(heros, item, 0))
 

#------------------------xxxxxxxxxxxxxxxxx----------------------------


# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

# listname.remove("item_name")
# listname.pop(index)
# listname.pop() ---> last item
# del listname[index]
# del listname --> del list
# listname.clear() ---> empty the list


key = "Black Panther"
heros.remove(key)
print(heros)

def getIndex(mylist, key):
    # index = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            return i
        
print(f'Hulk is at index {getIndex(heros, key="hulk")}')

insertAt(heros, key, getIndex(heros, key = 'hulk')+1)
print(heros)


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#    Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

heros = heros[:1] + ['doctor strange'] + heros[3:]
print(heros)


#------------------------xxxxxxxxxxxxxxxxx----------------------------


# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

sortedlist = sorted(heros)
print(sortedlist)

#------------------------xxxxxxxxxxxxxxxxx----------------------------

# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max_number = int(input("Enter a max number : "))
mylist = [i for i in range(1,max_number,2)]
print(mylist)