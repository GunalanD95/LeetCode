class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        
        cache = {}
        
        def bag_all(cur_house):
            if cur_house >= N:
                return 0
            if cur_house in cache:
                return cache[cur_house]
            cache[cur_house] = max(bag_all(cur_house+1),nums[cur_house]+bag_all(cur_house+2))
            return cache[cur_house]
        
        
        return bag_all(0)