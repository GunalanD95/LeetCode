class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N , K = len(s) , len(goal)
        if N != K:
            return False
        
        MOD  = 1000000007
        base = 27
        POW  = [1] * (max(N, K) + 1)
        
        for i in range(max(N, K)):
            POW[i+1] = (POW[i] * base)%MOD
            
            
        def generate_hash(w):
            n = len(w)
            code = 0
            for i in range(n):
                cur_char_acsci = ord(w[i]) - ord('a') + 1
                value = cur_char_acsci * POW[n-i-1]
                code += value
                code %= MOD
            return code
        
        pattern_hash = generate_hash(goal)
        
        
        s = s + s
        hash_sum = generate_hash(s[:K])
        
        if pattern_hash == hash_sum: return True
        
        
        left , right = 0 , K
        while right < N+N:
            hash_sum -= ((ord(s[left]) - ord('a') + 1) * POW[K-1])
            hash_sum *= (base)  % MOD
            hash_sum  %= MOD
            
            hash_sum += (( ord(s[right]) - ord('a') + 1 ))
            if pattern_hash == hash_sum: return True
            left  += 1
            right += 1
        
        return False
        
                