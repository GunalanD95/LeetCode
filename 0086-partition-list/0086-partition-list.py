# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        
        dummy2 = ListNode(-1)
        
        temp = head 
        temp1 = dummy1
        temp2 = dummy2
        
        while temp != None:
            newNode = ListNode(temp.val)
            if temp.val >= x:
                temp2.next = newNode
                temp2 = temp2.next
            else:
                temp1.next = newNode
                temp1 = temp1.next
            
            temp = temp.next
        
        temp1.next = dummy2.next
        print("dummy-1",dummy1.next)
        # print("dummy-2",dummy2.next)
        
        return dummy1.next
        