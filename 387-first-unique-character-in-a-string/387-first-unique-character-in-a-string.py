class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        
        # create freq of each char in a map
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1
                
                
        # iterate and then check 
        for j in range(len(s)):
            if hashmap[s[j]] == 1:
                return j
            
            
        return -1
                
                
    
                
        