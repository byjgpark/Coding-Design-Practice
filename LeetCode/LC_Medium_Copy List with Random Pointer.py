class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        # 1. Map old nodes to new nodes
        old_to_new = {}

        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # 2. Assign next and random pointers
        cur = head
        while cur:
            new_node = old_to_new[cur]
            new_node.next = old_to_new.get(cur.next)
            new_node.random = old_to_new.get(cur.random)
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