from collections import defaultdict

class Reverser:
    @staticmethod
    def rev(num):
        rev_num = 0
        while num > 0:
            last_digit = num % 10
            rev_num *= 10
            rev_num += last_digit
            num = num // 10
        return rev_num

class Solution:
    def countNicePairs(self, nums):
        N = len(nums)
        MOD = int(1e9) + 7

        reversed_nums = [Reverser.rev(num) for num in nums]
        differences = [num - rev_num for num, rev_num in zip(nums, reversed_nums)]
        occurrences = defaultdict(int)

        total = 0

        for diff in differences:
            occurrences[diff] += 1

        for count in occurrences.values():
            total += count * (count - 1) // 2

        return total % MOD
