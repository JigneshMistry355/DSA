expense = [
    
        ['Jan', 2200],
        ['Feb', 2350],
        ['Mar', 2600],
        ['Apr', 2130],
        ['May', 2190] 
    
]

#------------------------xxxxxxxxxxxxxxxxx----------------------------


#1 In Feb, how many dollars you spent extra compare to January?

extra = expense[1][1] - expense[0][1]
print(f'\nIn Feb, {extra} dollars were spent extra compared to January')


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#2 Find out your total expense in first quarter (first three months) of the year.

total = 0
for i in range(3):
    total = total + expense[i][1]
print(f'\nTotal expense in first quarter (first three months) of the year is {total}')


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#3 Find out if you spent exactly 2000 dollars in any month

extra = 0
flag = True
print()
for i in range(len(expense)):
    if expense[i][1] == 2000:
        print(f'\nExactly 2000 dollars were spent in the month of \"{expense[i][0]}\"')
    for j in range(len(expense)):
        extra = expense[i][1] - expense[j][1]
        if extra > 200:
            print(f'Extra 200 dollars were spent in the month of \"{expense[i][0]}\" than \"{expense[j][0]}\"')
            flag = False
        
if flag == True:
    print(f'\nExtra 200 dollars were spent in None of the months....')


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#4 June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(['Jun', 1900])
print(f'\nAfter the end of the month June, updated list is : ')
for i in range(len(expense)):
    print(f'{expense[i][0]} : {expense[i][1]}')


#------------------------xxxxxxxxxxxxxxxxx----------------------------


#5 You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

discount = 200
for i in range(len(expense)):
    if expense[i][0] == 'Apr':
        expense[i][1] -= 200
        break
print(f'\nUpdated list after altering April month is :')
for i in range(len(expense)):
    print(f'{expense[i][0]} : {expense[i][1]}')
