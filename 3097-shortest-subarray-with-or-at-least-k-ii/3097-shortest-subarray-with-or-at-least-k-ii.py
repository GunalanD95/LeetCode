class Solution:
    def AddToFreqMap(self, freq_count , cur_num):
        result = 0
        for idx in range(32):
            mask = 1 << idx
            if mask & cur_num:
                freq_count[idx] += 1
                
            if freq_count[idx]:
                result = result | 1 << idx
                
        return result
         
    def RemoveFromMap(self, freq_count, cur_num):
        result = 0
        for idx in range(32):
            mask = 1 << idx

            if mask & cur_num:
                freq_count[idx] -= 1

            if freq_count[idx] <= 0:
                result = result & ~(1 << idx)  
            else:
                result = result | (1 << idx)  

        return result
    
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        
        
        left = 0
        right = 0
        min_len = float('inf')
        
        freq_count = defaultdict(int, {i: 0 for i in range(32)}) # (bit_pos,cur_count)
        while right < N:
            cur_xor = self.AddToFreqMap(freq_count,nums[right])
            
            
            while left <= right and cur_xor >= k :
                cur_xor = self.RemoveFromMap(freq_count,nums[left])
                cur_len =  right - left + 1
                min_len =  min(min_len,cur_len)
                left += 1

            
            right += 1

        return -1 if min_len == float('inf') else min_len
        