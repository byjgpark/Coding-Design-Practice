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
        
        current = self.head
    
        self.head = newNode
        
        self.head.next = current
        
    def delete(self, data):
        current = self.head
        # while current.data == data: 
        print("check current.data", current.data)
        
        
        
if __name__ == "__main__":
    
    linkedList = LinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.prepend(0)
    linkedList.delete(0)
    # linkedList.display()
    
    
            
    
