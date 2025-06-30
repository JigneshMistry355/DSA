class Stack:

    def __init__(self, arr_size):
        self.arr_size = arr_size
        self.arr = [0] * self.arr_size
        self.top = -1

    def push(self, data):
        if self.top > self.arr_size -1:
            print("Stack overflow")
            return False
        self.top += 1
        self.arr[self.top] = data
        return True
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return 0
        return self.arr[self.top]
    
    def pop(self):
        if self.top == -1:
            print("Stack is empty")
            return False
        popped = self.arr[self.top]
        self.top -= 1
        return popped

    def display(self):
        if self.top == -1:
            print("stack is empty")
            return 0
        for i in range(self.top+1):
            print(self.arr[i], end=" ")
        print()


if __name__ == '__main__':
    stack = Stack(5)
    stack.push(2)
    stack.push(5)
    stack.push(8)
    stack.display()
    stack.pop()
    stack.display()
    # print("Top of the stack is ", stack.peek())
    
    print(stack.arr)
