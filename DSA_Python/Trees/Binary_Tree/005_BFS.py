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
    

    def BFS(self, value):
        if self.root is None:
            return False
        if self.root.data == value:
            return True
        queue = deque([self.root])
        while queue:
            temp_node = queue.popleft()
            print(temp_node.data, end=" ")
            if temp_node.data == value:
                return True
            if temp_node.left:
                queue.append(temp_node.left)
            if temp_node.right:
                queue.append(temp_node.right)
        return False
    
    def Level_Order(self):
        if self.root is None:
            return []
        res = []
        level = 0
        queue = deque([self.root])
        while queue:
            queue_len = len(queue)
            res.append([])
            for _ in range(queue_len):
                temp_node = queue.popleft()
                res[level].append(temp_node.data)
                
                if temp_node.left:
                    queue.append(temp_node.left)
                if temp_node.right:
                    queue.append(temp_node.right)
            level += 1
        return res


    
if __name__ == '__main__':
    root = Node(1)
    tree = Tree(root)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    print(tree.BFS(6))
    print(tree.Level_Order())
