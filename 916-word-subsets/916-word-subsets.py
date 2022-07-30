class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        d, ans = defaultdict(int), []

        for word in words2:                     #  <-- 1)
            c2 = Counter(word)
            for ch in c2:
                d[ch] = max(d[ch], c2[ch])

        for word in words1:                     #  <-- 2)
            c1 = Counter(word)

            for ch in d:
                if c1[ch] < d[ch]: break
            else:
                ans.append(word)                #  <-- else executes only if the for-loop
                                                #      completes without break

        return ans 
        