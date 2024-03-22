# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            
        # reverse the second half
        prev = None
        cur  = slow
        cn   = None
        while cur:
            cn = cur.next
            cur.next = prev
            prev = cur
            cur  = cn
            
            
        # compare head with prev (rev second half)
        while head and prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
            
            
        return True 
            