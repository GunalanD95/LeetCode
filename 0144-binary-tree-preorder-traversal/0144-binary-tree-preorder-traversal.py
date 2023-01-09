from collections import deque
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stack = []
        stack.append(root)
        ans   = []
        while stack:
            cur = stack.pop()
            ans.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)


        return ans