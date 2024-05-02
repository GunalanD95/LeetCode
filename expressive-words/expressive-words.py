from collections import defaultdict

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def compress(word):
            l_words  = []
            l_counts = []
            
            for char in word:
                if not l_words or l_words[-1] != char:
                    l_words.append(char)
                    l_counts.append(1)
                else:
                    l_counts[-1] += 1
                     
            return l_words , l_counts
            
        
        
        def is_strechy(word):
            nonlocal s_words , s_counts
            
            l_words , l_counts = compress(word)
            
            if l_words != s_words:
                return False
            
            for i in range(len(s_counts)):
                if s_counts[i] < 3 and l_counts[i] != s_counts[i]:
                    return False
                if s_counts[i] >= 3 and l_counts[i] > s_counts[i]:
                    return False
                
            return True
            
        
        
        s_words , s_counts = compress(s)
        
        total = 0
        for word in words:
            if is_strechy(word):
                total += 1
        return total
        
        