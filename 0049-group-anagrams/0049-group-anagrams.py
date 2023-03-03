from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)
        hmap = defaultdict(list)
        for i in range(N):
            count = [0] * 26
            for c in strs[i]:
                count[ord(c) - ord('a')] += 1
            hmap[tuple(count)].append(strs[i])
        ans = []
        for i in hmap:
            ans.append(hmap[i])
        return ans
