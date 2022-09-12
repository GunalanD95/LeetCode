class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i , j = 0 , len(numbers) - 1
        while i < j:

            cur_sum = numbers[i] + numbers[j]
            if cur_sum == target:
                return([i+1,j+1])

            elif cur_sum > target:
                if j < len(numbers) - 1:
                    while numbers[j] == numbers[j-1]:
                        j -= 1
                j -= 1   
                
            elif cur_sum < target:
                if i > 0: 
                    while numbers[i] == numbers[i+1]:
                        i += 1

                i +=1