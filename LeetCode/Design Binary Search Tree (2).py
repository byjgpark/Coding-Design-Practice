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
        
        # print("check node", node)

        if not node:
            return Node(key)
        
        if key < node.key:
            node.left = self.insert(node.left, key)
        else:    
            node.right = self.insert(node.right, key)
            
            print("check node at the end of insert function", node)
            
        return node    
        
    def inorder(self, node):
        
        if node:
            self.inorder(node.left)
            
            # print("check node.left", node)
            
            print(node.key, "=>", end=" ")
            
            self.inorder(node.right)
            
            # print(node.key, "=>", end=" ")
            
    def findMinValue(self, node):
        current = node
        while current.left:         
             current = node.left
        return current
        
    # delete 15
    def delete(self, node, key):
        
        if not node:
            return Node(key)
        
        if node.key > key:
            node.left = self.delete(node.left, key)
        elif node.key < key:
            node.right = self.delete(node.right, key)
        else:
            
            # if subtree has one node or None
            if not node.left:
                temp = node.right
                node = None
                return temp
            
            elif not node.right:
                temp = node.left
                node = None
                return temp
            
            # if subtress has two nodes
            temp = self.findMinValue(node.right)
            
            node.key = temp.key
            
            node.right = self.delete(node.right, temp.key)
            
        return node
            
            
        
if __name__ == "__main__":
    
    bs = BinarySearch()
    
    bs.root = None
    bs.root = bs.insert(bs.root, 20)
    bs.root = bs.insert(bs.root, 10)
    bs.root = bs.insert(bs.root, 30)
    bs.root = bs.insert(bs.root, 5)
    bs.root = bs.insert(bs.root, 15)
    bs.root = bs.insert(bs.root, 28)
    bs.root = bs.insert(bs.root, 35)
    bs.root = bs.insert(bs.root, 17)
    bs.root = bs.insert(bs.root, 13)
    
    # print("Check bs.root", bs.root)
    
    bs.root = bs.delete(bs.root, 10)
    
    print("Check inorder ", bs.inorder( bs.root))
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    # print("Check remove func", linkedList.remove(0))
    # linkedList.remove(0)
    # print("Get Values : ", linkedList.getValues())





