class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        front_node = self.findKthNode(head, k)
        end_node   = self.findKthNodeFromEnd(head, k)
        front_node.val, end_node.val = end_node.val, front_node.val
        return head

    def findKthNode(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        for _ in range(k-1):
            node = node.next
        return node
    
    def findKthNodeFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow_node = fast_node = head
        for _ in range(k-1):
            fast_node = fast_node.next
        while fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next
        return slow_node
