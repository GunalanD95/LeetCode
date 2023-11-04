class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        left_max_val  =  max(left) if left else 0
        right_max_val =  min(right) if right else 0
        
        if not right:
            return left_max_val
        if not left:
            return n-right_max_val
        return max(left_max_val,n-right_max_val)