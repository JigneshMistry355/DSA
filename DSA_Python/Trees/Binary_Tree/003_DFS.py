class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def DFS(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        left_res = self.DFS(node.left, key)
        right_res = self.DFS(node.right, key)
        return left_res or right_res
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

key = 6
result = root.DFS(root, key) 
print(f"{key} is present in the tree" if result else f"{key} is not present in the tree")