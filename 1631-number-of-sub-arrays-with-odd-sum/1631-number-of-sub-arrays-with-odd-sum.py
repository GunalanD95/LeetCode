class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        N  = len(arr)
        MOD = 10**9 + 7
        odd_sum = 0
        even_sum = 1

        cur_sum = 0
        total = 0
        for num in arr:
            cur_sum += num

            if cur_sum & 1:
                total += even_sum
                odd_sum += 1
            else:
                total += odd_sum
                even_sum += 1
                


        return total % MOD
        