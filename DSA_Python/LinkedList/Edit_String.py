myList = ['1One', 'Two/gbg', 'Three']

for i in range(len(myList)):
    for char in range(len(myList[i])):
        if not (myList[i][char].isalpha()):
            word = [i for i in myList[i]]
            for j in word:
                if not(j.isalpha()):
                    word.remove(j)
            word = "".join(word) 
            myList[i] = word
            break
print(myList)