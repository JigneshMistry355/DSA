expense = [
    
        ['Jan', 2200],
        ['Feb', 2350],
        ['Mar', 2600],
        ['Apr', 2130],
        ['May', 2190] 
    
]

# In Feb, how many dollars you spent extra compare to January?

Feb_expense = 0
Jan_expense = 0

for i in range(len(expense)):

    if expense[i][0] == "Feb":
        Feb_expense = expense[i][1]
        print(f'Expense for month of Feb is ::: {Feb_expense}') 
        
    if expense[i][0] == "Jan":
        Jan_expense = expense[i][1]
        print(f'\nExpense for the month of Jan is ::: {Jan_expense}')
        
print(f'\nIn Feb, \"{Feb_expense - Jan_expense}\" dollars are spent extra compared to January ')


# Find out your total expense in first quarter (first three months) of the year.

total = 0
for i in range(3):
    total = total + expense[i][1]
print(f'\nTotal expense in first quarter (first three months) of the year is ::: {total}\n')


# Find out if you spent exactly 2000 dollars in any month

month = ''
for i in range(len(expense)):
    if expense[i][1] == 2000:
        month = month + str(expense[i][0])
        break
if month != '':
    print(f'Exactly 2000 dollars are spent in the month of {month}\n')
else:
    print(f'Exactly 2000 dollars are spent in none of the month\n')


# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print("Updated expense after month of June")    
expense.append(['June', 1980])
for i in range(len(expense)):
    print(expense[i])

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list

updated_Apr_expense = 0
for i in range(len(expense)):
    if expense[i][0] == 'Apr':
        updated_Apr_expense = expense[i][1] - 200
        break
print(f'\nThe updated expense of month April is ::: {updated_Apr_expense}')
