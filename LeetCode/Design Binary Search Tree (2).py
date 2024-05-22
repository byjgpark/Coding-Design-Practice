
class Node:
    def __init__(self,key, left, right):
        self.key = key
        self.left = left
        self.right = right
    
    def insert(self, node, key) -> object:
    
        
        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = insert(node.left, key)
        else:    
            node.right = insert(node.right, key)
            
        return node    
        
    # def inorder(node):
    
    
    

if __name__ == "__main__":
    
    root = None
    root = insert(root, 8)
    root = insert(root, 8)
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    # print("Check remove func", linkedList.remove(0))
    # linkedList.remove(0)
    # print("Get Values : ", linkedList.getValues())





