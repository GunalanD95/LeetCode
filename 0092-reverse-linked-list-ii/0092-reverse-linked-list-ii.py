# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reve(self,head,k):
        
        if not head.next or not head:
            return head 

        # 3 pointer approach 
        prev = head 
        cur = head.next 

        prev.next = None 
        count = 1
        while cur != None and count < k:
            print("ciunt",count,k)
            cn = cur.next 
            cur.next = prev 
            prev = cur 
            cur = cn 
            count += 1

            
        return prev , cur
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right or not head:
            return head  
        
        # create dummy node to avoid edge cases
        dummy = ListNode(0,head)
        
        # get left pointer node 
        count = 1
        temp = dummy
        
        head_point = dummy
        cur  = head 
        while count < left:
            temp = temp.next
            count += 1
            
        head_point = temp
        cur = temp.next

        link_head , link_tail = self.reve(cur,right - left + 1)
        
        head_point.next = link_head
        cur.next = link_tail
        
        
        return dummy.next
        