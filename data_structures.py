# data_structures.py
class Node:
    def __init__(self, left, right, item):
        self.left = left
        self.right = right
        self.item = item

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(None, None, data)
        if data < root.item:
            root.left = self.rinsert(root.left, data)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        node = self.rsearch(self.root, data)
        if node:
            print(f"{data} found!")
        else:
            print(f"{data} not found!")
        return node

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root is not None:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root is not None:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root is not None:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

    def delete_min(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current

    def delete_max(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current

    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return None
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self.delete_min(root.right)
            root.item = temp.item
            root.right = self.rdelete(root.right, temp.item)
        return root

    def size(self):
        return len(self.inorder())

class SimpleStack(list):
    def is_empty(self):
        return len(self) == 0
    
    def push(self, data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("Stack is empty --- cannot pop")
    
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("Stack is empty --- cannot peek")
    
    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No insertion possible in stack (use push instead)")

class SimpleQueue:
    def __init__(self):
        self.item = []
    
    def is_empty(self):
        return len(self.item) == 0
    
    def enqueue(self, data):
        self.item.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        return None
    
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        return None
    
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        return None
    
    def size(self):
        return len(self.item)
    
    def clear(self):
        self.item.clear()
