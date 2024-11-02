class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        N = len(sentence)
        
        first_word = sentence[0]
        last_word  = sentence[-1]
        
        for i in range(1,N):
            prev = sentence[i-1]
            cur  = sentence[i]
            
            if prev[-1] != cur[0]:
                return False
            
            
        return last_word[-1] == first_word[0]