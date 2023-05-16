# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        
        count = 2
        
        prev  = None
        cur   = head
        
        while cur and count > 0:
            cn = cur.next
            cur.next =  prev
            prev = cur
            cur  = cn
            count -= 1
            
            
        if head:
            head.next = self.swapPairs(cur)

        return prev
    