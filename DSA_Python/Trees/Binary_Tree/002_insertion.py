from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    
class Tree:
    def __init__(self, root):
        self.root = root


    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return 
        queue = deque([self.root])
        while queue:
            temp_node = queue.popleft()
            if temp_node.left is None:
                temp_node.left = Node(data)
                temp_node.left.parent = temp_node
                break
            else:
                queue.append(temp_node.left)
            if temp_node.right is None:
                temp_node.right = Node(data)
                temp_node.right.parent = temp_node
                break
            else:
                queue.append(temp_node.right)
        return self.root
    

    def inorder(self, node:Node):
        if node is None:
            return None
        self.inorder(node.left)
        print(node.data, end=" ") 
        self.inorder(node.right)


if __name__ == '__main__':
    root = Node("A")
    tree = Tree(root)
    tree.insert("B")
    tree.insert("C")
    tree.insert("D")
    tree.inorder(root)