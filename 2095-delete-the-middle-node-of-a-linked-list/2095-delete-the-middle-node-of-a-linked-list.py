class Node:
    def __init__(self,val,next= None):
        self.val = val 
        self.next = next 
        

        
class Solution:
    def findlength(self,head):
        count = 0
        
        temp = head
        
        while temp:
            temp = temp.next 
            count += 1
            
        return count 
    
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        if not head.next.next:
            head.next = None
            return head
        
        
        res_len = self.findlength(head)
        to_check = (res_len // 2) 
        to_check -= 1
        
        temp = head
        while to_check != 0:
            temp = temp.next
            to_check -= 1
            
        print("to_delete_node",temp.val)
        newNode = temp.next
        temp.next = newNode.next
        
        
        return head
            
        