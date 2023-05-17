class Solution:
    def findMid(self,head):
        prev = None
        slow = fast = head 
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        return prev , slow 
    
    
    def reverse(self,head):
        prev = None
        cur  = head
        cn   = None
        
        while cur:
            cn = cur.next
            cur.next = prev
            prev = cur
            cur  = cn
            
        return prev
    
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        h1_tail , h2 = self.findMid(head)
        h1_tail.next = None
        
        h2 = self.reverse(h2)
        
        max_sum = 0
        while head and h2:
            cur_sum = head.val + h2.val
            max_sum = max(max_sum,cur_sum)
            
            head = head.next
            h2   = h2.next
            
        return max_sum
        
          