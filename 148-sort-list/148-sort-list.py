import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    def mergeLL(self,list1,list2):
        if not list1: return list2
        if not list2: return list1
        if not list1 and list2: return None
        
        head = None
        if list1.val < list2.val:
            head  = list1
            list1 = list1.next
        else:
            head  = list2
            list2 = list2.next
        
        temp = head
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1     = list1.next
            else:
                temp.next = list2
                list2     = list2.next                
                
            temp = temp.next
        
        if list1:
            temp.next = list1
        else:
            temp.next = list2
            
        return head
    
    def getMid(self, head):
        if not head:
            return

        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head 
        
        
        mid      = self.getMid(head)
        newNode  = mid.next
        mid.next = None 
        
        
        left     = self.sortList(head)
        
        right    = self.sortList(newNode)
        
        
        return self.mergeLL(left,right)
        