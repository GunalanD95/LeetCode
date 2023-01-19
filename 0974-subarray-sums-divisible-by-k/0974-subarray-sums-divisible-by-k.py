class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        count   = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        cur_sum = 0
        for i in nums:
            cur_sum += i
            
            rem = cur_sum % k
            
            if rem < 0:
                rem += k 
            
            count += hashmap[rem]
            
            hashmap[rem] += 1
            
            
        return count 
        