class Solution:
    def digit_sum(self,num):
        cur_sum = 0
        while num:
            cur_sum += num % 10
            num = num // 10
        return cur_sum
    def countLargestGroup(self, n: int) -> int:
        hmap = defaultdict(int)
        max_val = 0
        for num in range(1,n+1):
            cur = self.digit_sum(num)
            hmap[cur] += 1
            max_val = max(max_val,hmap[cur])

        total = 0
        for val in hmap:
            if hmap[val] == max_val:
                total += 1

        return total
        