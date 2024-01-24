class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        total = 0

        def is_palindrome(counts):
            odd_count = 0
            for c in counts:
                if c % 2 != 0:
                    odd_count += 1
                if odd_count > 1:
                    return False
            return True

        def dfs(root, counts):
            nonlocal total
            if not root:
                return

            counts[root.val - 1] += 1

            if not root.left and not root.right:
                if is_palindrome(counts):
                    total += 1

            dfs(root.left, counts)
            dfs(root.right, counts)

            counts[root.val - 1] -= 1

        dfs(root, [0] * 9) 
        return total