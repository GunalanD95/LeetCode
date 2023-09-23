class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        N = len(words)

        wordMap = defaultdict(int)
        words.sort(key=lambda x: len(x))
        
        res = 0
        for word in words:
            wordMap[word] = 1  
            
            for index in range(len(word)):
                new_word = word[:index] + word[index+1:]
                
                if new_word in wordMap:
                    wordMap[word] = max(1 + wordMap[new_word], wordMap[word])
                
            res = max(res, wordMap[word])
                
        return res
            
            
            
            
            

        

