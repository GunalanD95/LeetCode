class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = set(banned)
        
        arr  = []
        
        for i in range(1,n+1):
            if i not in seen:
                arr.append(i)
                
        N = len(arr)
        
        count = 0
        cur_sum  = 0
        for num in arr:
            if cur_sum + num <= maxSum:
                cur_sum += num
                count += 1
            else:
                break

        return count
        