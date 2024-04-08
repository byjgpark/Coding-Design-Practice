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
        
    def delete(self, key):
        # print("check self.head", self.head)
        current_node = self.head
        # If head node itself holds the key to be deleted
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        # Search for the key to be deleted, keep track of the previous node
        prev_node = None
        while current_node and current_node.data != key:
            # print("Check current_node", current_node)
            # print("Check current_node.data", current_node.data, "check key", key)
            prev_node = current_node
            # print("Check prev_node", prev_node)
            current_node = current_node.next
            # print("Check current_node.data", current_node.data, "check key", key)
            # print("Check current_node.data", current_node.data, "check key", key)
            print("Check prev_node at the line of while-loop : ", prev_node)
            print("Check current_node at the line of while-loop : ", current_node)
        # If key was not present in linked list
        
        # print("Check current_node before the last if-statement : ", current_node)
        if current_node is None:
            return
        # Unlink the node from linked list
        prev_node.next = current_node.next
        current_node = None
        
if __name__ == "__main__":
    
    linkedList = LinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    # linkedList.prepend(0)
    # linkedList.delete(0)
    # linkedList.delete(1)
    linkedList.delete(5)
    # linkedList.delete(3)
    linkedList.display()
    
    
            
    
