class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        max_sum = [0] * (N + 1)

        def solvethis(indx):
            if indx == N:
                return 0

            if max_sum[indx] != 0:
                return max_sum[indx]

            max_val = float('-inf')
            max_sum_value = 0

            for i in range(indx, min(indx + k, N)):
                max_val = max(max_val, arr[i])
                cur_sum = (i - indx + 1) * max_val + solvethis(i + 1)
                max_sum_value = max(max_sum_value, cur_sum)

            max_sum[indx] = max_sum_value
            return max_sum_value

        return solvethis(0)