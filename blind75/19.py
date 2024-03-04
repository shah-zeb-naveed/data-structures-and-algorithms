# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return

        # new solution

        dummy = ListNode(0, head)
        l, r = dummy, head
        
        while n > 0:
            n -= 1
            r = r.next
        
        # gap between r and l is now n + 1

        while r:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return dummy.next

        
        
        # # old solution
        # index_to_pointer = dict()

        # i = 1
        # node = head
        # while node.next:
        #     index_to_pointer[i] = node
        #     node = node.next
        #     i += 1
        
        # # sz = i
        # to_be_removed = i - (n - 1)
        # if to_be_removed == 1:
        #     new_head = head.next
        #     head.next = None
        #     return new_head
        
        # parent_of_to_be_removed = to_be_removed - 1
        # index_to_pointer[parent_of_to_be_removed].next = \
        # index_to_pointer[parent_of_to_be_removed].next.next

        # return head
