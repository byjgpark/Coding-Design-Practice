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
            i+=1
            # previ = curr
            curr = curr.next
        print("check curr :", curr)
        curr.next = curr.next.next
        
    #     # print("check self.head :", self.head)
    
        
    #     # print("Check previ", previ)
        
    #     # print("check ")
        
    #     # previ.next = previ.next.next
        
    #     # self.head
    
    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        
        print("check self.head", self.head)
        
        while i < index and curr:
            i += 1
            curr = curr.next
        
        print("check curr :", curr)
        # Remove the node ahead of curr
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
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
    linkedList.remove(1)
    print("Get Values : ", linkedList.getValues())