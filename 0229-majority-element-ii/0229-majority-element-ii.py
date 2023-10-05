class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        
        if N == 1:
            return [nums[0]]
        
        me_1 = nums[0]
        me_2 = nums[1]
        me_count1 = 0
        me_count2 = 0
        
        
        for num in nums:
            if num == me_1:
                me_count1 += 1
            elif num == me_2:
                me_count2 += 1
            else:
                if me_count1 == 0:
                    me_count1 = 1
                    me_1 = num
                    
                elif me_count2 == 0:
                    me_count2  = 1
                    me_2 = num
                else:
                    me_count1 -= 1
                    me_count2 -= 1                    
        check_1 = 0
        check_2 = 0 
        for num in nums:
            if num == me_1: check_1 += 1
            if num == me_2: check_2 += 1
        
        print(me_count2,me_2,check_2,N//3)
        if check_1 > N//3 and check_2 > N//3 and me_1 != me_2:
            return [me_1,me_2]
        elif check_1 > N//3:
            return [me_1]
        elif check_2 > N//3:
            return [me_2]
            
        
        