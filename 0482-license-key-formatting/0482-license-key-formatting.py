class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        
        count = 0
        
        res   = []
        cur   = ''
        
        for char in s[::-1]:
            if char == '-':
                continue
            else:
                cur = char.upper() + cur
                count += 1
                if count == k:
                    res.append(cur)
                    cur = ''
                    count = 0
         
        if not res:
            return cur
        res = res[::-1]
        ans = "-".join(res)
        if len(cur) > 0:
            ans = cur + '-' + ans        
        return ans