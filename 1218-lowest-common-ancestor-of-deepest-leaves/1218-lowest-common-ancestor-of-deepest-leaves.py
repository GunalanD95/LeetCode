from collections import defaultdict
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_lca(node):
            if not node:
                return 0 , None

            left_dep  , left_lca  = find_lca(node.left)
            right_dep , right_lca = find_lca(node.right)

            if left_dep > right_dep:
                return left_dep+1 , left_lca
            elif left_dep < right_dep:
                return right_dep+1 , right_lca
            else:
                return right_dep+1 , node


        return find_lca(root)[1]