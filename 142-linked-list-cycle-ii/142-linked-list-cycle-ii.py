class Solution:
    def checkCycle(self,head):
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return fast
            
        return None        
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None 
        
        
        fast = self.checkCycle(head)
        
        if not fast: return fast
        print("yes")
        slow = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
            
            
        return slow 