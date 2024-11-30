class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = len(nums)
        counter = Counter(nums)
        sorted_nums = sorted(counter.keys())        
        
        @cache
        def find_max(indx):
            if indx >= len(sorted_nums):
                return 0
            
            # dont take
            skip = find_max(indx+1)
            
            # take it 
            take = sorted_nums[indx] * counter[sorted_nums[indx]]
            
            if indx+1 < len(sorted_nums) and sorted_nums[indx+1] == sorted_nums[indx]+1:
                take += find_max(indx+2)
            else:
                take += find_max(indx+1)
        
            return max(skip,take)
        
        return find_max(0)
        