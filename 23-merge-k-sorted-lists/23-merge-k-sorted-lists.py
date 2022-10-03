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
        N = len(lists)
        if N == 0: return None
        if N == 1: return lists[0]
        
        root = lists[0]
        for i in range(1,N):
            cur   = lists[i]
            root  = self.mergeLL(root,cur)
        return root 
            
            
            
            
            
            
            
        
        
        
        
        
        
        
        