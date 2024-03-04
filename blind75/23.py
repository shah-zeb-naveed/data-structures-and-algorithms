# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy_id = 1 # just to avoid invalid comparison of nodes. else override <= operator

        if not lists or len(lists) == 0:
            return None
        # TRYING MIN-HEAP
        # O(N * K * LOG K) (CHATGPT: KLOGK + NLOGK)AND O (K)
        # init heap
        import heapq
        q = [] # I recall that heap can be stored in array with specific indices pointing to child nodes
        # K * LOG K
        for i in range(len(lists)):
            dummy_id += 1
            if lists[i] is not None:
                heapq.heappush(q, (lists[i].val, dummy_id, lists[i])) # if same vals, then error coz of node comparison
        
        # init new list pointer
        dummy = ListNode(0)
        prev = dummy

        # pop
        # O(N)
        while q:
            # O(LOG K)
            cur = heapq.heappop(q)[2]
            prev.next = cur
            prev = cur
            if cur.next is not None:
                dummy_id += 1
                # O(LOG K)
                heapq.heappush(q, (cur.next.val, dummy_id, cur.next))
        
        return dummy.next


        # KIND OF MERGE SORT
        # N: NUMBER OF ALL ELEMENTS
        # K NUMBER OF LISTS
        # # O(LOG K * N)

        # def merge(l1, l2):
        #     dummy = ListNode(0)
        #     prev = dummy

        #     while l1 and l2:
        #         if l1.val <= l2.val:
        #             prev.next = l1
        #             l1 = l1.next
        #         else:
        #             prev.next = l2  
        #             l2 = l2.next

        #         prev = prev.next
            
        #     if l1:
        #         prev.next = l1
            
        #     if l2:
        #         prev.next = l2
            
        #     return dummy.next
        
        # # THIS IS KIND OF MERGE SORT BECAUSE WE AVOID REPEATED WORK
        # while len(lists) > 1:
        #     merged_lists = []
        #     for i in range(0, len(lists), 2):
        #         l1 = lists[i]
        #         l2 = lists[i + 1] if (i + 1) < len(lists) else None
        #         merged_lists.append(merge(l1, l2))
            
        #     lists = merged_lists
        # return lists[0]
        

                
        