# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        if not list1 and list2: return None
        
        # vote head
        head = None
        if list1.val < list2.val: 
            head  = list1 
            list1 = list1.next
        else:
            head  = list2
            list2 = list2.next
            
        # start merging 
        tail = head
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1     = list1.next
            else:
                tail.next = list2
                list2     = list2.next
                
            tail = tail.next
            
            
        # attach left over
        if list1: 
            tail.next = list1
        else: 
            tail.next = list2
            
            
        return head
        