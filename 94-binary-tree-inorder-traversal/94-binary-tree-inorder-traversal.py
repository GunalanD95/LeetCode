# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return
        else:
            ar = []
            self._inorderTrav(root,ar)
        return ar
        


    def _inorderTrav(self,curNode,ar):
        if curNode.left:
            self._inorderTrav(curNode.left,ar)
        ar.append(curNode.val)
        if curNode.right:
            self._inorderTrav(curNode.right,ar)
        
        