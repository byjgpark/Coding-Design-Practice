# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Node:
     # Constructor method
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return f"Check self.data : {self.data} || self.next : {self.next}"    

class LinkedList:
    
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        
        if not self.head:
            self.head = newNode
            return
        current = self.head
        
        while current.next:
            current = current.next
        current.next = newNode 
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end =" -> ")
            current = current.next
        print("end")
        
    def prepend(self, data):
        newNode = Node(data)
        
        print("Check newNode", newNode)
        
        current = self.head
        
        print("Check current", current)
    
        self.head = newNode
        
        print("Check self.head", self.head)
        
        self.head.next = current
        
        print("---------------------------------------------")
        
    def delete(self, key):
        
        current_node = self.head
        # Checking the 1st node contain the key 
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            # current_node = None ?? is it necessary 
            return 
        
        previ_node = None
        # Search for the key to be deleted and keep tracking of the previ node 
        while current_node and current_node.data != key:
            previ_node = current_node
            current_node = current_node.next
            print("check previ_node : ", previ_node)
            print("check current_node : ", current_node)
            
        if current_node is None:
            return
        
        previ_node.next = current_node.next
        current_node = None
        
if __name__ == "__main__":
    
    linkedList = LinkedList()
    # linkedList.append(1)
    # linkedList.append(2)
    # linkedList.append(3)
    linkedList.prepend(1)
    linkedList.prepend(2)
    # linkedList.delete(0)
    # linkedList.delete(1)
    # linkedList.delete(2)
    # linkedList.delete(3)
    # linkedList.delete(5)
    linkedList.display()
    
    
            
    
