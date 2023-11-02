# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        total_count = 0

        def dfs(node):
            nonlocal total_count
            if not node:
                return 0, 0

            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)

            sub_tree_count = 1 + left_count + right_count
            sub_tree_sum = node.val + left_sum + right_sum

            sub_tree_average = sub_tree_sum // sub_tree_count

            if sub_tree_average == node.val:
                total_count += 1

            return sub_tree_count, sub_tree_sum

        dfs(root)
        return total_count