# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        oddDummy1  = ListNode(-1)
        evenDummy1 = ListNode(-2)
        
        temp = head
        oddDummy = oddDummy1
        evenDummy = evenDummy1
        count = 1
        while temp:
            if count & 1:
                oddDummy.next = temp
                oddDummy = oddDummy.next
            else:
                evenDummy.next = temp
                evenDummy = evenDummy.next
                
            temp = temp.next
            count += 1
        
        evenDummy.next = None
        oddDummy.next  = evenDummy1.next
        
        
        return oddDummy1.next