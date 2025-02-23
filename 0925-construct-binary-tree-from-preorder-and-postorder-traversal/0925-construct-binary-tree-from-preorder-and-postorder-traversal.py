# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def initialize_root_index(self,postorder):
        hmap = defaultdict(int)
        for idx in range(len(postorder)):
            hmap[postorder[idx]] = idx
        return hmap

    def constructTree(self,l,r):
        if self.pre_idx >= len(self.preorder) or l > r:
            return None
        root_val = self.preorder[self.pre_idx]
        root = TreeNode(root_val)
        self.pre_idx += 1
        if l == r:
            return root

        left_val = self.preorder[self.pre_idx]
        left_idx = self.root_map[left_val]
        root.left  = self.constructTree(l, left_idx) 
        root.right = self.constructTree(left_idx+1,r-1)
        return root

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.root_map = self.initialize_root_index(postorder)
        self.preorder , self.postorder = preorder , postorder
        self.pre_idx = 0  # Pointer to track root in preorder
        # pre  -> root , left , right
        # post -> left , right , root
        return self.constructTree(0, len(postorder) - 1)
