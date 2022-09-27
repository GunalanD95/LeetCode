class Solution:
    def findlength(self,head):
        count = 0
        
        temp = head 
        while temp:
            temp = temp.next
            count += 1
            
        return count
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        N = self.findlength(head)
        
        to_find = (N//2) 
        
        temp = head
        while to_find != 0:
            temp = temp.next
            to_find -= 1
            
        return temp
        
        
        