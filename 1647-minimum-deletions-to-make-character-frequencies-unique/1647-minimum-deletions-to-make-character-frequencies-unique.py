class Solution:
    def minDeletions(self, s: str) -> int:
        hmap = Counter(s)
            
        seen = set()
        res = 0
        for char in hmap:
            count = hmap[char]
            while count in seen:
                count -= 1
                res += 1
            if count > 0:
                seen.add(count)
                
        return res