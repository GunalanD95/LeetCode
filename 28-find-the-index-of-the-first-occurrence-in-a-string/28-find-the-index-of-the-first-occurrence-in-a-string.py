class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s , text = haystack , needle
        N , k = len(s) , len(text)
        MOD = 1000000007
        base = 27

        POW = [1] * (max(N, k) + 1)

        for i in range(max(N, k)): 
            POW[i + 1] = (POW[i] * base) % MOD 


        def hashcode(w):
            n = len(w)
            code = 0
            for i in range(n):
                value = ((ord(w[i]) - ord('a') + 1) * POW[n-i-1]) 
                code += value
                code %= MOD

            return code


        # pattern value - hash_sum value 
        pattern_hash = hashcode(text)

        # inital window of size k - hash_sum
        hash_sum = hashcode(s[:k])
        if hash_sum == pattern_hash: 
            return 0 
        # sliding window calculation 
        low , right = 0 , k


        while right < N:
            
            hash_sum -= ((ord(s[low]) - ord('a') + 1) * POW[k-1])


            hash_sum *= (base)  % MOD 
             
            hash_sum  %= MOD

            hash_sum += (( ord(s[right]) - ord('a') + 1 ))


            if pattern_hash == hash_sum:
                return low + 1


            low += 1
            right += 1

        return -1