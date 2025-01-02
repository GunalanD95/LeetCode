class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a','e','i','o','u'}
        n  = len(words)
        pf = [0] *  n
        pf[0] = 1 if words[0][0] in vowels and words[0][-1] in vowels else 0
        for idx in range(1,n):
            if words[idx][0] in vowels and words[idx][-1] in vowels:
                pf[idx] = 1 + pf[idx-1]
            else:
                pf[idx] = pf[idx-1]

        print("pf",pf)
        ans = []
        for l,r in queries:
            left_side  = 0
            right_side = pf[r]

            if l-1 >= 0:
                left_side = pf[l-1]            
            ans.append(right_side-left_side)

        return ans