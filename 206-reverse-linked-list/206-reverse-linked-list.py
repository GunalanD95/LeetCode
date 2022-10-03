class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # no node 
        if not head:
            return head
        # single node 
        prev = None
        cur = head
        cn  = None
        
        
        
        while cur:
            cn   =  cur.next
            cur.next = prev
            prev  = cur
            cur   = cn
        
            
                
                
        return prev
        
        