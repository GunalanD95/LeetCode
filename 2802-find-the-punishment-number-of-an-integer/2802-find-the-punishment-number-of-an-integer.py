class Solution:
    def canPartition(self, s, target , index,cur_sum) -> bool:
        if index == len(s):
            return cur_sum == target
        num = 0
        for i in range(index,len(s)):
            num = num * 10 + int(s[i])
            if cur_sum + num > target:
                break
            if self.canPartition(s, target, i + 1, cur_sum + num):
                return True
        return False

    def punishmentNumber(self, n: int) -> int:
        total = 0
        for num in range(1,n+1):
            square_str = str(num * num)
            if self.canPartition(square_str, num, 0, 0):
                total += num * num
        return total