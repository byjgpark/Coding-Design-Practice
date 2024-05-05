# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        print("check prev =", prev)
        print("check curr =", curr)# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        print("check prev outside of while :", prev)
        print("check curr outside of while :", curr)

        while curr:
            print("check 1st prev in the beginning :", prev)
            print("check 1st curr in the beginning :", curr)
            temp = curr.next
            print("check 1st temp in the while-loop :", temp)
            curr.next = prev
            print("check 2nd curr in the while-loop :", curr)
            print("check curr.next in the while-loop :", curr.next)
            prev = curr
            print("check 2nd prev in the while-loop :", prev)
            curr = temp
            print("check 2nd temp at the end of while-loop :", temp)
            print("check 3rd curr at the end of while-loop :", curr)
            print("------------------------------------------------------------------------------------------------------")
        # print("check prev outside of while-loop", prev)
        return prev


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
