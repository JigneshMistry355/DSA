heros=['spider man','thor','hulk','iron man','captain america']

#------------------------xxxxxxxxxxxxxxxxx----------------------------
# Length of the list 
count = 0
for i in heros:
    count += 1
print(f'Length of list is {count}')


#------------------------xxxxxxxxxxxxxxxxx----------------------------

# Add 'black panther' at the end of this list

heros.append('black panther')
print(heros)

#------------------------xxxxxxxxxxxxxxxxx----------------------------


# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'

heros.remove('black panther')
for i in range(len(heros)):
    if heros[i] == 'hulk':
        heros.insert(i+1,'black panther')
print(heros)


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#    Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.

to_be_deleted = ['hulk', 'thor']
heros = [x for x in heros if x not in to_be_deleted]
heros.append('doctoer strange')
print(heros)

#------------------------xxxxxxxxxxxxxxxxx----------------------------


# Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


heros.sort()
print(heros)

#------------------------xxxxxxxxxxxxxxxxx----------------------------

# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

user_input = input("Enter any number : ")
if user_input.isnumeric():
    print([i for i in range(1,int(user_input),2)])
else:
    print('not a number')
    