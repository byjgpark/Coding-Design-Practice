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
        
        # print("check curr :", curr)
        # print("check new_node :", new_node)
        if not curr.next.next:
            self.tail = curr.next
        # print("check curr.next :", curr.next)
        # print("check self.tail :", self.tail)
        # print("--------------------------------------------------------------------------------------------------------------------------------")
        # print("Check new node", new_node)
        # print("check curr", curr)
    
    def insertTail(self, val: int) -> None:
        
        # print("Check self.head from insertTail", self.head)
        # print("check self.tail from insertTail", self.tail)
        
        self.tail.next = Node(val)
        self.tail = self.tail.next
        # print("check self from insertTail", self.head)
        # print("Check self.head", self.head)
        
    def remove(self, index: int) -> bool:
        
        curr = self.head
        i = 0
        while i < index and curr:
            curr = curr.next
            i += 1
        
        # print("Check curr", curr)
        print("Aftet Check curr", curr)
        while curr and curr.next:
            curr.next = curr.next.next
            
            if not curr.next:
                self.tail = curr
                print("Check self.tail", self.tail)
            return True
        return False

    def getValues(self) -> list[int]:
        
        print("check self.tail from getValues function :", self.tail)
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.data)
            curr = curr.next
        return arr
        
if __name__ == "__main__": 
    linkedlist = LinkedList()
    linkedlist.insertHead(1)
    linkedlist.insertHead(2)
    linkedlist.insertHead(4)
    # linkedlist.insertTail(9)
    # linkedlist.insertTail(12)
    # linkedlist.insertTail(25)
    # linkedlist.insertTail(25)
    linkedlist.remove(2)
    # linkedlist.insertHead(5)
    print("check values ", linkedlist.getValues())