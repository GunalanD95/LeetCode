class Solution:
    def mergeLL(self,list1,list2):
        dummy = ListNode(-1)
        
        cur = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
                
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
            
        if list1:
            cur.next = list1
        else:
            cur.next = list2
            
            
        return dummy.next
        
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l =  self.mergeKLists(lists[:mid]) 
        
        r =   self.mergeKLists(lists[mid:])
        
        
        return self.mergeLL(l, r)
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        