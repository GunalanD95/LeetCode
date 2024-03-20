# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        a_node = None
        b_node = None
        
        temp = list1
        for _ in range(a-1):
            temp = temp.next
            
        a_node = temp
        
        temp = list1 
        for _ in range(b):
            temp = temp.next
        
        b_node = temp
        
        while temp.next:
            temp = temp.next
        
        last_node = list2
        while last_node.next:
            last_node = last_node.next
        
        a_node.next = list2
        last_node.next = b_node.next
        b_node.next = None
        
        
        return list1
        