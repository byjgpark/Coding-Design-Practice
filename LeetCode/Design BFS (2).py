class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    def __str__(self):
        return f"check data : {self.data} || left : {self.left} || right : {self.right}"
        
class BFS:
    def __init__(self):
        self.root = None
        
    def height(self, root):
        
        if not root:
            return 0
        
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1
        
    def helpPrintBFS(self, root):
        
        height = self.height(root)
        for i in range(1, height+1):
            self.printDataBFS(root, i)
            
    def printDataBFS(self, root, height): 
        if not root:
            return
        if height == 1:
            print(root.data, end='-> ')
        elif height > 1:
            self.printDataBFS(root.left, height-1)
            self.printDataBFS(root.right, height-1) 
        
if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    
    bts = BFS()

    print("check root tree",root)

    print("check height of tree :", bts.height(root))
    
    bts.helpPrintBFS(root)
    
    
    
