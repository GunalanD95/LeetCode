class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        tokens.sort()
        n = len(tokens)
        
        left , right = 0 , n -1
        
        score = 0
        maxscore = 0
        
        while left <= right:
            left_token = tokens[left]
            right_token = tokens[right]
            
            if power >= left_token:
                power -= left_token
                score += 1
                left += 1
                maxscore = max(score,maxscore)
                
            elif score >= 1:
                power  += right_token
                score -= 1
                right -= 1
                
            else:
                break
                
                
        return maxscore