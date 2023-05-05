class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        q = deque()
        q.append(root)

        while q:
            prev_val = None
            for _ in range(len(q)):
                cur_node = q.popleft()
                if cur_node:
                    # check if the current value follows the pattern for the current level
                    if (level % 2 == 0 and (cur_node.val % 2 == 0 or (prev_val and cur_node.val <= prev_val))) or \
                       (level % 2 == 1 and (cur_node.val % 2 == 1 or (prev_val and cur_node.val >= prev_val))):
                        return False
                    
                    prev_val = cur_node.val
                    q.append(cur_node.left)
                    q.append(cur_node.right)

            level += 1
            
        return True
