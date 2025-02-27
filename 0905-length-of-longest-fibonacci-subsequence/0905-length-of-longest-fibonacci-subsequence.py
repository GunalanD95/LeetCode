from collections import Counter

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        N = len(arr)
        max_count = 0

        hmap = Counter(arr)

        def fib(a:int ,b:int) -> int:
            c = a+b
            if c not in hmap:
                return 0
            return 1 + fib(b,c)

        for i in range(N):
            for j in range(i+1,N):
                count = 2
                count += fib(arr[i],arr[j])
                if count > 2:
                    max_count = max(max_count,count)
    
        return max_count 