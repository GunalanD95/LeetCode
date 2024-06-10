class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        maxval = max(heights)
        count = [0 for _ in range(maxval + 1)]
        for height in heights:
            count[height] += 1

        for height in range(1, maxval + 1):
            count[height] += count[height - 1]

        ans = 0 
        
        for height in heights:
            if height != heights[count[height] - 1]:
                ans +=  1
            count[height] -= 1
        return ans