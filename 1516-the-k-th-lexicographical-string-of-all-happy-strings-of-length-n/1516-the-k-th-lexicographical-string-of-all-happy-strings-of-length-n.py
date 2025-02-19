class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def generate_substring(cur):
            if len(cur) >= n:
                res.append("".join(cur))
                return

            for char in 'abc':
                if not cur or cur[-1] != char:
                    cur.append(char)
                    generate_substring(cur)
                    cur.pop()

        generate_substring([])

        if k > len(res):
            return ""
        res.sort()
        return res[k-1]