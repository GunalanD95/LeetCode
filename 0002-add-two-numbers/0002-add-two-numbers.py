# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = 0

        tmp1 , tmp2 = l1 , l2

        dummyNode = ListNode(-1)
        temp = dummyNode

        while tmp1 or tmp2:
            val1 = tmp1.val if tmp1 else 0
            val2 = tmp2.val if tmp2 else 0

            total_sum = val1 + val2 + carry

            cur_sum = total_sum % 10

            carry = total_sum // 10
            temp.next = ListNode(cur_sum)

            if tmp1:
                tmp1 = tmp1.next
            if tmp2:
                tmp2 = tmp2.next
            temp = temp.next
        
        if carry:
            temp.next = ListNode(carry)

        return dummyNode.next