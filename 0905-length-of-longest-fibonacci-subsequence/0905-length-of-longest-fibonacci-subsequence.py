from collections import defaultdict
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        lookup = {}
        for i in range(n):
            lookup[arr[i]] = i

        longest = defaultdict(lambda: 2)
        ans = 0
        for i in range(n):
            a = arr[i]
            for j in range(i+1,n):
                b = arr[j]
                c = a + b

                if c in lookup:
                    longest[(j,lookup[c])] = longest[(i,j)] + 1

                    ans = max(ans,longest[(j,lookup[c])])


        return ans 

                


        


        