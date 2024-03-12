# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        cumsum = 0
        d = {0: dummy}
        cur = head

        # Populate dictionary
        # If same cumsum found, we can drop previous value as is represents subsequence that can sum to 0
        # In above commented example: we see cumsum reach 3 twice(l_idx=1, r_idx=3). This implies we can drop idx2 & idx3 as they sum to 0
        # Hence we update dictionary with latest value
        while cur:
            cumsum += cur.val
            d[cumsum] = cur
            cur = cur.next

        # Form final linked list
        # Impt point to note is we take d[cumsum].next. 
        # In above example, we want to drop idx2 & idx3, so we have cur.next point to d[cumsum].next
        # i.e: cur.next = node(idx3).next, effectively dropping idx2 and idx3
        cur = dummy
        cumsum = 0
        while cur:
            cumsum += cur.val
            cur.next = d[cumsum].next
            cur = cur.next
        return dummy.next
                
        
        
                
        
        
        