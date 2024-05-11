# Definition for singly-linked list.
class ListNode1:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:

        # dummy = node = ListNode()
        dummy = ListNode()
        node = dummy

        print("check dummy =", dummy)
        print("check node =", node)

        while list1 and list2:
            print("check list1.val =", list1.val)
            print("check list2.val =", list2.val)
            # print("check list1 =", list1)
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
                print("check node inside of if-statement :", node)
                print("check dummy inside of if-statement :", dummy)
                print("check list1 inside of while-loop :",list1)
            else:
                node.next = list2
                list2 = list2.next
                print("check node inside of else-statement :",node)
                print("check dummy inside of else-statement :", dummy)
                print("check list2 inside of while-loop :",list2)
            print("Check node inside of while-loop =", node)
            node = node.next
            print("Check node after node = node.next inside of while-loop =", node)
 
        # node.next = list1 or list2
        if list1:
            node.next = list1
            print("check list if")
        elif list2:
            node.next = list2
            print("check list elif list2")
        
        print("Check node =", node)
        print("Check dummy =", dummy)

        return dummy.next