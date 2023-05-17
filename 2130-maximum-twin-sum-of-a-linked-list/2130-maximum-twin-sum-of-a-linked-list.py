class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        indexMap = {}
        N = 0
        temp = head
        
        while temp:
            indexMap[N] = temp.val
            temp = temp.next
            N += 1
            
        max_sum = 0
        for i in range(N):
            cur_sum = (indexMap[i] + indexMap[N-i-1])
            max_sum = max(max_sum,cur_sum)
        return max_sum    