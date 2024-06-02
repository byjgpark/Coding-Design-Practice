# Binary Search Tree operations in Python

# Create a node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"Node key : {self.key} | left : {self.left} | right : {self.right}"

# Inorder traversal
def inorder(root):
    if root is not None:
        # Traverse left
        inorder(root.left)

        # Traverse root
        print(root.key, "->", end=' ')

        # Traverse right
        inorder(root.right)

# Insert a node
def insert(node, key):
    
    # print("check node =", node)
    
    # print("Check node at the beginning of function :", node, "&& it's key", key)

    # Return a new node if the tree is empty
    if node is None:
        return Node(key)
    # print("Check node.left = ", node.left)
    # print("Check node.right = ", node.right)
    
    # print("check node.key :", node.key)
    
    # print("hey check here 123")
    
    # print("Check left count :", left)

    # Traverse to the right place and insert the node
    # 1 < 3
    if key < node.key:
        node.left = insert(node.left, key)
        # print("check node.left inside if-statement",node.left)
    elif key > node.key:
        node.right = insert(node.right, key)
        # print("check node.right inside if-statement",node.right)
    elif key == node.key:
        print("they are same !!!")
        
    # print("Check node at the end of function :", node)
        
    # print("--------------------------------------------------------")

    return node


# Find the inorder successor
def minValueNode(node):
    current = node
    
    print("check current inside of function :", current)
    print("check current.left inside of function :", current.left)
    # Find the leftmost leaf
    while(current.left is not None):
        print("check current.left inside of while :", current.left)
        current = current.left

    print("check minValueNode", current)
    return current

# Deleting a node
def deleteNode(root, key):

    # Return if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted
    
    # three edge cases when the value is found
    # 1. its root has only one child or no child
    # 2. its root has two child
    # 2.1 find the inorder successor 
    
    
    # 1. 10 < 20 O
    # 2. 10 < 10 X
    if key < root.key:
        root.left = deleteNode(root.left, key)
        print("check root in the root.left recursion :", root)
        print("check root.left in the root.left recursion :", root.left)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        print("check root in the recursion :", root)
        print("check root.right in the root.right recursion :", root.right)
    # when the value is found 
    else:
        # If the node is with only one child or no child
        
        print("Check the root in the else-statement", root)
        
        if root.left is None:
            print("Check root in the root.left :", root)
            print("Check root.right in the root.left :", root.right)
            temp = root.right
            root = None
            print("Check temp in the root.left :",temp)
            return temp

        elif root.right is None:
            print("Check temp in the root.right :", root.left)
            temp = root.left
            root = None
            return temp
        
        print("Check root right before temp varible :", root)
        print("Check root.right right before temp varible :", root.right)
    
        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)
        
        print("check temp here", temp)
        
        print("check root after temp", root)

        root.key = temp.key
        
        print("check root right before root.right variable :", root)
        
        print("check root.right right before root.right variable :", root.right)
        
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
        
    print("check root at the end of function :", root)
        
    print("check root.right at the end of function :", root.right)

    return root


if __name__ == "__main__": 

    root = None
    root = insert(root, 20)
    root = insert(root, 10) 
    root = insert(root, 30)
    root = insert(root, 5)
    root = insert(root, 15)
    root = insert(root, 28)
    root = insert(root, 35)
    root = insert(root, 17)
    root = insert(root, 13)
    

    # root = deleteNode(root, 10)
    
    print("Check final root", root)

    print("Inorder traversal: ", end=' ')
    inorder(root)

    # print("\nDelete 10")
    # root = deleteNode(root, 10)
    # print("Inorder traversal: ", end=' ')
    # inorder(root)