# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        def reverse_recursively(node):
            new_head = node
            if node.next:
                new_head = reverse_recursively(node.next)
                node.next.next = node

            node.next = None
            return new_head
        
        return reverse_recursively(head)

        #dummy = ListNode(0, head)
        prev, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

        # node = head
        # stack = []
        # while node:
        #     stack.append(node)
        #     node = node.next
        
        # head = stack.pop()
        # head.next = None
        # prev_node = head
        # while stack:
        #     new_node = stack.pop()
        #     prev_node.next = new_node
        #     prev_node = new_node
        # prev_node.next = None

        # return head


        