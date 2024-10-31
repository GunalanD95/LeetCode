class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        
        cur  = set()
        for i,word in enumerate(startWords):
            startWords[i] = "".join(sorted(word))
            cur.add(startWords[i] )
            
        for i,word in enumerate(targetWords):
            targetWords[i] = "".join(sorted(word))
            
            
        res = 0
        for word in targetWords:
            for i in range(len(word)):
                if word[:i] +  word[i+1:] in cur:
                    res += 1
                    break

        return res