class Solution:
    
    def check(self,people,boats,limit):
        count_multiple = 0
        count_single = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if i == j: # handle case where only one person is left
                count_single += 1
                break
            if people[i] + people[j] <= limit:
                count_multiple += 1
                i += 1
                j -= 1
            else:
                count_single += 1
                j -= 1
        return count_multiple + count_single <= boats

        
        
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people) 
        people.sort()
        low      = 1
        high     = N 
        ans      = 0
        while low <= high:
            mid = (low + high)//2
            if self.check(people,mid,limit):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans