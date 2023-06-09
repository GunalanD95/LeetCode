class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        
        low , high =  0 , N -1
        
        ans = ''

        while low <= high:
            mid = (low + high) // 2

            if ord(letters[mid]) > ord(target):
                ans = letters[mid]
                high = mid - 1
            else:
                low = mid + 1
        
        if not ans:
            return letters[0]
        return ans