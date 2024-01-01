class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        total = 0

        g.sort()
        s.sort()

        g_pointer = 0
        s_pointer = 0

        while g_pointer < len(g) and s_pointer < len(s):
            child_want = g[g_pointer]
            c_we_have = s[s_pointer]

            if c_we_have >= child_want:
                total += 1
                g_pointer += 1 
            s_pointer += 1

        return total
