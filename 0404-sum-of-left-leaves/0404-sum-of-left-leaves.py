from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append((root,'r'))
        
        cur_sum = 0
        while q:
            for _ in range(len(q)):
                cur_node , dire = q.popleft()
                if cur_node.left:
                    q.append((cur_node.left,'l'))
                if cur_node.right:
                    q.append((cur_node.right,'r'))
                 
                if dire == 'l' and (not cur_node.left and not cur_node.right):
                    cur_sum += cur_node.val
                 
                 
                 
        return cur_sum