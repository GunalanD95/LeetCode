# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev = None
        cur = head
        cn  = None
        while cur:
            cn   =  cur.next
            cur.next = prev
            prev  = cur
            cur   = cn     
        return prev
    
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        rev_head = self.reverse(head)
        
        dummy_node = ListNode(rev_head.val)
        max_val    = rev_head.val
        
        temp1 = dummy_node
        temp2 = rev_head.next
        while temp2:
            if temp2.val >=  max_val:
                max_val = temp2.val
                temp1.next = ListNode(temp2.val)
                temp1 = temp1.next
            temp2 = temp2.next
            
        return self.reverse(dummy_node)
            
            
        
        