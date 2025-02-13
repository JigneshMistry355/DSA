class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item) 

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


    # if we want to import this stack class into another file 
    #then we would have problem with the code that is definded here...because that would also run inour imported file
if __name__ == "__main__":#if this is the main file that is being run then execute the following code 
    s = Stack() #instance of the Stack class
    print("Printing stack: ",s)
    print("Is the stack empty ",s.is_empty())
    s.push(1)
    s.push(2)
    s.push(3)
    print("Pushed items of the stack: ",s)
    #s.pop()
    print("Poping an item: ",s.pop())
    print("After pop",s)
    print("Return the top of the stack: ",s.peek())
    print("printing the size of the stack: ",s.size())
    