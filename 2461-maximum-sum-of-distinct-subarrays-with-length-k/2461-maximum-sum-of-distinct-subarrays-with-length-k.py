class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k > N: return 0
        
        cur_sum = 0
        hashmap = defaultdict(int)
        
        for idx in range(k):
            hashmap[nums[idx]] += 1
            cur_sum += nums[idx]
            
        max_sum = float('-inf') if len(hashmap) != k else cur_sum
        
        left    = 0
        for right in range(k,N):
            hashmap[nums[left]] -= 1
            cur_sum -= nums[left]
            
            if hashmap[nums[left]] == 0:
                del hashmap[nums[left]]
                
            hashmap[nums[right]] += 1
            cur_sum += nums[right]
            if len(hashmap) == k:
                max_sum = max(max_sum,cur_sum)
            left += 1
        
        return max_sum if max_sum != float('-inf') else 0
            
            
        