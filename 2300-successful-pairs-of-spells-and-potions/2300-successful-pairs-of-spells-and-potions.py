class Solution:
    def binary_search(self,arr,success,spell):
        low , high = 0 , len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] * spell >= success:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans 
    
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        N = len(potions)
        ans = []
        for num in spells:
            value = self.binary_search(potions,success,num)
            if value != -1:
                ans.append(N-value)
            else:
                ans.append(0)
        return(ans)        