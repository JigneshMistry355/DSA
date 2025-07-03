class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


    def addLeft(self, child):
        child.parent = self
        self.left = child


    def addRight(self, child):
        child.parent = self
        self.right = child


    def inorder_traversal(self, child):
        if child is None:
            return 
        child.inorder_traversal(child.left)
        print(child.data, end=" ")
        child.inorder_traversal(child.right)

    
    def preorder_traversal(self, child):
        if child is None:
            return
        
        print(child.data, end=" ")
        child.preorder_traversal(child.left)
        child.preorder_traversal(child.right)


    def postorder_traversal(self, child):
        if child is None:
            return
        child.postorder_traversal(child.left)
        child.postorder_traversal(child.right)
        print(child.data, end=" ")


    # gives level of a particular node, not the depth of tree
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
            p = p.parent
            level += 1
        return level
    

    # def printTree(self):
    #     space = " " * self.getLevel() * 3
    #     prefix = space + "|__" if self.parent else ""
    #     print(prefix + str(self.data))
        
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

a.addLeft(b)
a.addRight(c)

b.addLeft(d)
b.addRight(e)

c.addLeft(f)
c.addRight(g)

d.addLeft(h)

print("Level of tree: ",h.getLevel())

print("\n\n\nIn-order traversal")
a.inorder_traversal(a)

print("\n\n\nPost-order traversal")
a.postorder_traversal(a)

print("\n\n\nPre-order traversal")
a.preorder_traversal(a)

