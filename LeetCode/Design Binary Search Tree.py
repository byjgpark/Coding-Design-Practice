class Node():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def insert(node, value):
    if node is None:
        return Node(value)
    if value < node.data:
        node.left = insert(node.left, value)

def inOrderTraverse(node):
    if node is not None:
        inOrderTraverse(node.left)
        print(node.data)
        inOrderTraverse(node.right)
        
        
if __name__ == "__main__":
    node = Node(5)
    node.left = Node(3)
    node.right = Node(7)
    node.left.left = Node(2)
    node.left.right = Node(4)
    node.right.left = Node(6)
    node.right.right = Node(8)
    
    inOrderTraverse(node)
    
    