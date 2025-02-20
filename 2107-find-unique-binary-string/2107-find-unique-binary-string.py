class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        seen = set(nums)
        n = len(nums[0])
        def check_set_bit(num,indx):
            mask = 1 << indx
            if mask & num:
                return True
            return False

        subarry_len = 2**n
        for i in range(subarry_len):
            cur = ''
            for j in range(n):
                if check_set_bit(i,j):
                    cur += '1'
                else:
                    cur += '0'

            if cur not in seen:
                return cur

            seen.add(cur)

        return ""

        