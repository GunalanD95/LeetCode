# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self,head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length
    
        
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        length = self.get_len(head)
        k = k % length
        mid_point = length - k 
        
        temp = head
        prev = None
        while mid_point > 0:
            prev = temp
            temp = temp.next
            mid_point -= 1
        
        if not temp:
            return head
        prev.next = None
        
        new_tail = temp
        while new_tail and new_tail.next:
            new_tail = new_tail.next
            
        new_tail.next = head
        return temp
        