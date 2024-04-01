from functools import cmp_to_key
def custom_compartor(x,y):
    n , m  = len(x) , len(y)
    if n < m:
        return -1
    elif n > m:
        return 1
    else:
        for i in range(n):
            if x[i] < y[i]:
                return -1
            elif y[i] < x[i]:
                return 1
            else:
                continue

    return 0

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        key = cmp_to_key(custom_compartor)
        nums.sort(key=key,reverse=True)
        print(nums)
        return nums[k-1]