# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def find_node(node):
            if not node:
                return False

            check_root = False
            if node.val == p.val or node.val == q.val:
                check_root = True

            left  = find_node(node.left)
            right = find_node(node.right)

            print(left,node.val,right,"check_root",check_root)
            if (left and right) or (check_root and (left or right)):
                self.ans = node
                return False
            return check_root or left or right

        find_node(root)
        return self.ans