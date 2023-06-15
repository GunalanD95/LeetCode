# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append(root)
        
        maxSum = float('-inf')
        levelNum = 1
        maxLevel = 1
        while q:
            levelSum = 0
            for _ in range(len(q)):
                cur_node = q.popleft()
                levelSum += cur_node.val
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)

            if levelSum > maxSum:
                maxSum    = levelSum
                maxLevel  = levelNum
            levelNum += 1
        return maxLevel