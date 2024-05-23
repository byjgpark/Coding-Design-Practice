
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
    
    def __str__(self):
        return f"Node key : {self.key} | left : {self.left} | right : {self.right}"
    
class BinarySearch: 
    def __init__(self):
        self.root = None
       
    def insert(self, node, key) -> object:

        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:    
            node.right = self.insert(node.right, key)
            
        return node    
        
    def inorder(self, node):
        
        if node:
            
            
            
            self.inorder(node.left)
            
            # print("check node.left", node)
            
            self.inorder(node.right)
            
            print(node.key, "=>", end=" ")

        
if __name__ == "__main__":
    
    bs = BinarySearch()
    
    bs.root = None
    bs.root = bs.insert(bs.root, 8)
    bs.root = bs.insert(bs.root, 3)
    bs.root = bs.insert(bs.root, 1)
    bs.root = bs.insert(bs.root, 4)
    bs.root = bs.insert(bs.root, 9)
    
    print("Check bs.root", bs.root)
    
    bs.inorder(bs.root)
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    # print("Check remove func", linkedList.remove(0))
    # linkedList.remove(0)
    # print("Get Values : ", linkedList.getValues())





