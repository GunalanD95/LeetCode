class Solution:
    def isSimilar(self,string1,string2) -> bool:
        if string1 == string2:
            return True
        diff = 0
        for i in range(len(string1)):
            if string1[i]  != string2[i]:
                diff += 1
                
                if diff > 2:
                    return False
        
        if diff == 0 or diff == 2:
            return True
        return False
    
    def dfs(self,string,visited,arr):
        if string in visited:
            return
        
        visited.add(string)
        
        N = len(arr)
        for i in range(N):
            if self.isSimilar(string,arr[i]):
                self.dfs(arr[i],visited,arr)
        return count
        
    def numSimilarGroups(self, strs: List[str]) -> int:
        N = len(strs)
        
        res  = 0
        seen = set()
        for char in strs:
            if char not in seen:
                self.dfs(char,seen,strs)
                res += 1
                
        return res