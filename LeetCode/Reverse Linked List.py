# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        print("check prev =", prev)
        print("check curr =", curr)

        while curr:
            temp = curr.next
            print("check 1st temp in the while-loop", temp)
            curr.next = prev
            print("check curr.next in the while-loop", curr.next)
            prev = curr
            print("check prev in the while-loop", prev)
            curr = temp
            print("check curr at the end of while-loop", curr)

            print("------------------------------------------------------------------------------------------------------")
        # print("check prev outside of while-loop", prev)
        return prev
