# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        nodes = []
        def bst(node):
            if not node:
                return
            bst(node.left)
            nodes.append(node.val)
            bst(node.right)
            
        bst(root)
        
        def bstcreater(l,r):
            if l >= r:
                return None
            print(l,r)
            mid = (l + r)// 2
            root_node = TreeNode(nodes[mid])
            root_node.left = bstcreater(l,mid)
            root_node.right = bstcreater(mid+1,r)
            print("nodes[mid]",nodes[mid])
            return root_node
        
        res = bstcreater(0,len(nodes))
        return res
        
        