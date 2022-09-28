# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_len(self,head,k):
        count = 0
        
        temp = head
        
        while temp:
            temp = temp.next
            count += 1
        
        print("count",count)
        return count - k
        
        
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next and n == 1:
            return None
        
        ref = head
        res_len = self.get_len(head,n)
        print("res_len",res_len)
        temp = head
        while temp and res_len != 1:
            temp = temp.next
            res_len -= 1
        
        if not temp: return ref.next
        
        node_to_add = temp.next
        temp.next = node_to_add.next
        
        return head