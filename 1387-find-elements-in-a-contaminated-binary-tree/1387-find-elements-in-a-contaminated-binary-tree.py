# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def dfs(self,node,seen):
        if not node:
            return
        seen.add(node.val)
        if node.left:
            node.left.val = 1 + 2*node.val 
        if node.right:
            node.right.val = 2 + 2*node.val
        self.dfs(node.left,seen)
        self.dfs(node.right,seen)

    def __init__(self, root: Optional[TreeNode]):
        root.val = 0
        self.seen = set()
        self.dfs(root,self.seen)

    def find(self, target: int) -> bool:
        if target in self.seen:
            return True
        return False


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)