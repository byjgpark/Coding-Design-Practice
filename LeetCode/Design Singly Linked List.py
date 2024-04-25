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
        # print("check self.data", self.head)
        # new_node = Node(val)
        # print("check new_node", new_node)
        # curr = self.head.next
        # curr = new_node
        # print("check curr", curr)
        # self.head.next = new_node
        # # self.head.next = curr
        # print("check self.head.next", self.head.next)
        
        new_node = Node(val)
        
        print("check new_node : ", new_node)
        new_node.next = self.head.next
        print("check new_node : ", new_node)
        self.head.next = new_node
        # new_node.next = self.head.next
        # self.head.next = new_node
        
        print("check self.head", self.head)
        print("------------------------------------------")
        
        

    # def insertTail(self, val: int) -> None:
        

    # def remove(self, index: int) -> bool:
        

    # def getValues(self) -> List[int]:
        

       
if __name__ == "__main__":
    linkedList = LinkedList()
    linkedList.insertHead(3)
    linkedList.insertHead(1)
    # linkedList.insertHead(0)
    # linkedList.insertTail(9)
    # linkedList.insertTail(4)
    # linkedList.insertTail(2)
    # linkedList.remove(3)
    # print("Get Values : ", linkedList.getValues())