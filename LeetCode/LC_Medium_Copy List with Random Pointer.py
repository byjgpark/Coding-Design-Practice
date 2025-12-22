class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __repr__(self):
        return f"Node(val={self.val}, next={self.next.val if self.next else None}, random={self.random.val if self.random else None})"

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        print("check head =", head)

        # 1. Map old nodes to new nodes
        old_to_new = {}

        cur = head
        while cur:
            # print("Check cur =", cur)
            old_to_new[cur] = Node(cur.val)
            print(f"created {old_to_new[cur]} from old Node(val={cur.val}) id={id(cur)}")
            cur = cur.next
            print(f"moved to {cur} id={id(cur) if cur else None}")
            # print(f"created {old_to_new[cur]} from old Node(val={cur.val}) id={id(cur)}")

        # 2. Assign next and random pointers
        cur = head
        while cur:
            print(f"old_to_new = {old_to_new}")
            print(f"check cur = {cur} id={id(cur)}")
            print(f"check old_to_new obj ={old_to_new[cur]}")
            new_node = old_to_new[cur]
            print(f"check new_node = {new_node}")
            print(f"check cur.next = {cur.next}")
            new_node.next = old_to_new.get(cur.next)
            print(f"check new_node.next = {new_node.next}")
            print(f"check old_to_new.get(cur.next = {old_to_new.cur.next}")
            new_node.random = old_to_new.get(cur.random)
            print(f"check new_node.random = {new_node.random}")
            cur = cur.next

        # 3. Return head of new list
        return old_to_new[head]

if __name__ == '__main__':
    # head = Node(1, Node(2, Node(3)))
    # head.random = head.next.next
    # head.next.random = head
    # head.next.next.random = head.next

    # sol = Solution()
    # new_head = sol.copyRandomList(head)

    # ## Check the result
    # cur = new_head
    # while cur:
    #     print(cur.val, end=' ')
    #     if cur.random:
    #         print(f'({cur.random.val})', end=' ')
    #     else:
    #         print('(None)', end=' ')
    #     cur = cur.next
    # print()

    ## I want to [[7,null],[13,0],[11,4],[10,2],[1,0]] test
    head = Node(7, Node(13, Node(11, Node(10, Node(1)))))
    head.random = None
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head

    sol = Solution()
    new_head = sol.copyRandomList(head)

    ## Check the result
    cur = new_head
    while cur:
        print(cur.val, end=' ')
        if cur.random:
            print(f'({cur.random.val})', end=' ')
        else:
            print('(None)', end=' ')
        cur = cur.next
    print()