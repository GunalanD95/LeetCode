class Solution:
    def findAnagrams(self, s2: str, s1: str) -> List[int]:
        countA = Counter(s1)
        k = len(s1)
        n = len(s2)
        
        
        countB = Counter()
        for i in range(min(k,n)):
            if s2[i] in countA:
                countB[s2[i]] += 1

        ans = []
        if countA == countB: ans.append(0)
            
        left = 0
        for right in range(k,n):
            countB[s2[left]] -= 1
            if countB[s2[left]] <= 0:
                del countB[s2[left]]
                
            if s2[right] in countA:
                countB[s2[right]] += 1
            
            # print("left",left,countA,countB)
            if countA == countB: ans.append(left+1)
            left += 1
            
        return ans 