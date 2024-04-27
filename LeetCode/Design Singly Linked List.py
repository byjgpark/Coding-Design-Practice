# Singly Linked List Node
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 

    def __str__(self):
        return f"Node's self.data = {self.data} and self.next = {self.next}"
        
class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    # def get(self, index: int) -> int:
        
    def insertHead(self, val: int) -> None:
        
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        
        if not new_node.next:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        
    def remove(self, index: int) -> bool:
        
        curr = self.head
        i = 0
        while i < index:
            curr = curr.next
            i+=1
        
        print("check self.head", self.head)
        print("check curr", curr)
        
        self.head.next = curr.next
        
        print("after check self.head", self.head)
        # while curr:
            # print("hey check here")
            
            
        

    def getValues(self) -> list[int]:
        # print("check self.head", self.head)
        curr = self.head
        # print("cherck curr", curr)
        arr = []
        while curr and curr.next:
            arr.append(curr.next.data)
            curr = curr.next
            # print("Check curr in the while-loop", curr)
        return arr
    
if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertHead(3)
    linkedList.insertHead(1)
    linkedList.insertHead(4)
    linkedList.insertTail(9)
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    linkedList.remove(2)
    print("Get Values : ", linkedList.getValues())