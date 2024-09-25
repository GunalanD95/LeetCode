from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0

        if not root:
            return total

        q = deque()
        q.append((root,root.val))

        while q:
            for _ in range(len(q)):
                cur_node , max_val = q.popleft()
                if cur_node.val >= max_val:
                    max_val = cur_node.val
                    total += 1
                if cur_node.left:
                    q.append((cur_node.left,max_val))

                if cur_node.right:
                    q.append((cur_node.right,max_val))

        return total