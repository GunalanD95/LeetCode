class Solution:
    def reverse(self,head):
        prev = None
        cur  = head
        cn   = None
        while cur:
            cn = cur.next
            cur.next = prev
            prev = cur
            cur = cn
        return prev
    
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head 
        revhead  = self.reverse(head)
        carry    = 0
        temp = revhead
        prev = None
        while temp:
            cur_val = (temp.val * 2) % 10
            cur_car = (temp.val * 2) // 10
            temp.val = cur_val + carry
            carry    = cur_car
            prev  = temp
            temp = temp.next
        if carry:
            newHead = ListNode(carry)
            prev.next = newHead
        return self.reverse(revhead)