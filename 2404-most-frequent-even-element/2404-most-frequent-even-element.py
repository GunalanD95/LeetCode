class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        hashmap = {}

        for i in nums:
            if i % 2 == 0:
                if i in hashmap:
                    hashmap[i] += 1
                else:
                    hashmap[i] = 1


        max_val = float('-inf')
        ans = []
        max_key = -1
        for j in hashmap:
            if hashmap[j] > max_val:
                max_val = hashmap[j]
                max_key = j
                
   
        return max_key
                    
        
        