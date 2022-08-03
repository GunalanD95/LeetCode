class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        N = len(arr)
        if N == 1: return 1

        cur_c = 0
        i = 0
        cur_sum = 0
        org_sum = 0
        while i < N:
            org_sum += arr[i]
            cur_sum += i
            if org_sum == cur_sum:
                cur_c +=1

            i += 1
            
        return (cur_c)