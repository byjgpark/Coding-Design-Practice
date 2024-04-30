class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f"Check self.data = {self.data}, self.next = {self.next}"

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    # def get(self, index: int) -> int:
            

    def insertHead(self, val: int) -> None:
        
        new_node = Node(val)
        curr = self.head
        new_node.next = curr.next
        curr.next = new_node
        
        print("check curr", curr)
        print("check self.tail", self.tail)
        
        print("--------------------------------------------------------------------------------------------------------------------------------")
        # print("Check new node", new_node)
        # print("check curr", curr)
        
        
        
        

    # def insertTail(self, val: int) -> None:
        

    # def remove(self, index: int) -> bool:
        

    # def getValues(self) -> List[int]:


if __name__ == "__main__": 
    linkedlist = LinkedList()
    linkedlist.insertHead(1)
    linkedlist.insertHead(2)
    # linkedlist.insertHead(5)