class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:        
        hmap =  defaultdict()
        for index , char in enumerate(order):
            hmap[char] = index 
            
            
        def helper(word1,word2):
            count = 0
            N, M  = len(word1) , len(word2)
            min_len = min(N,M)
            for i in range(min(len(word1),len(word2))):
                if hmap[word1[i]] <= hmap[word2[i]]:
                    if hmap[word1[i]] == hmap[word2[i]]:
                        count += 1
                    pass
                else:
                    return False
            print("count",count,min_len)
            if count == min_len and len(word1) > len(word2):
                return False
            return True 
            
        
        N = len(words)
        for idx in range(1,N):
            pre = words[idx-1]
            cur = words[idx]
            
            if hmap[pre[0]] < hmap[cur[0]]:
                pass
            
            elif hmap[pre[0]]  == hmap[cur[0]]:
                if helper(pre,cur):
                    pass
                else:
                    return False
                
            else:
                return False
            
        return True