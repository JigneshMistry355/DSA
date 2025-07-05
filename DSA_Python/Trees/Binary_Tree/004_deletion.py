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
    

    def delete(self, val):
        if self.root is None:
            return False
        queue = deque([self.root])
        target = None
        while queue:
            temp_node = queue.popleft()
            if temp_node.data == val:
                target = temp_node
                break
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        if target is None:
            return self.root
        queue = deque([self.root])
        last_node = None
        last_parent = None
        while queue:
            temp_node = queue.popleft()
            last_node = temp_node
            last_parent = temp_node.parent
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        target.data = last_node.data
        if last_parent:
            if last_parent.left == last_node:
                last_parent.left = None
            else:
                last_parent.right = None
        else:
            return None
        return self.root

    
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    tree = Tree(root)
    
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    
    tree.inorder(root) # 4 2 5 1 3 
    print()
    tree.delete(3)
    tree.inorder(root) # 4 2 1 5
    
