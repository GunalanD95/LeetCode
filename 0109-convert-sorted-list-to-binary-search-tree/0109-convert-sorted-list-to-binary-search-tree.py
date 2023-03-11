# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        
        
        def convertSorted(l,r,arr):
            if l == r:
                return
            
            mid = (l+r)//2
            
            root = TreeNode(arr[mid])
            root.left  = convertSorted(l,mid,arr)
            root.right = convertSorted(mid+1,r,arr)
            
            return root
        
        return convertSorted(0,len(arr),arr)
            