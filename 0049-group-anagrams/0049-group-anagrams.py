from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs)
        
        hmap = defaultdict(list)
        for i in range(N):
            cur_char = strs[i]
            new_list = sorted(cur_char)
            new_char = "".join(new_list)
            hmap[new_char].append(cur_char)
            
            
        print("hmap",hmap)
        ans = []
        for i in hmap:
            ans.append(hmap[i])
        return ans 
            
        