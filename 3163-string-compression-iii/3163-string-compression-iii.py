from collections import Counter
class Solution:
    def compressedString(self, word: str) -> str:
        N = len(word)
        
        word_map = Counter(word)
        
        cur_idx  = 0
        res = []
        
        while cur_idx < N:
            cur_char = word[cur_idx]
            count    = 1
            
            while cur_idx+1 < N and word[cur_idx+1] == cur_char:
                count +=1 
                cur_idx += 1
                if count == 9:
                    break
                
            
            
            print(cur_char,count,cur_idx)
            res.append(str(count)+cur_char)
            cur_idx += 1
        
        return "".join(res)