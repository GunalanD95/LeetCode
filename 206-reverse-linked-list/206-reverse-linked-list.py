class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        # no node 
        if not head:
            return head
        # single node 
        if not head.next:
            return head 
        
        # two node 
        if not head.next.next:
            temp = head
            newhead = temp.next
            temp.next = None
            newhead.next = temp
            head = newhead
            return head
        
        # 3 pointer method 
        prev = head
        cur  = head.next
        head.next  = None # head will become tail initally

        while cur != None:
            cn  = cur.next
            cur.next = prev 
            prev = cur
            cur = cn 
            
                
                
        return prev
        
        