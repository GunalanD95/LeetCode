class Solution:
    def swapNodes(self, head, k) :
        front_node = self.findKthNode(head, k)
        end_node   = self.findKthNodeFromEnd(head, k)
        front_node.val, end_node.val = end_node.val, front_node.val
        return head

    def findKthNode(self, head, k) :
        node = head
        for _ in range(k-1):
            node = node.next
        return node
    
    def findKthNodeFromEnd(self, head, k) :
        slow = fast = head
        for _ in range(k-1):
            fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        return slow
