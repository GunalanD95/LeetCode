class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        lo = [] # max_heap
        hi = [] # min_heap
        to_remove = defaultdict(int)
        def top(tp):
            if tp == 'lo':
                return -1 * lo[0]
            else:
                return hi[0]

        # do setup
        for i in range(k):
            heappush(lo, -1 * nums[i])
            heappush(hi, top('lo'))
            heappop(lo)
            if len(hi) > len(lo):
                heappush(lo, -1 * top('hi'))
                heappop(hi)

        res = []

        def get_median():
            if k % 2 == 1:
                return top('lo')
            else:
                return (top('lo') + top('hi')) / 2

        for i in range(k, n+1):
            res.append(get_median())

            if i == n:
                return res
    
            balance = 0
            rem_ele = nums[i - k]
            add_ele = nums[i]
            i+=1

            ## remove
            if rem_ele <= top('lo'):
                balance -= 1
            else:
                balance += 1
            to_remove[rem_ele] += 1

            ## add num
            if lo and add_ele <= top('lo'):
                balance += 1
                heappush(lo, -1 * add_ele)
            else:
                balance -= 1
                heappush(hi, add_ele)
            
            # balance
            if balance < 0:
                heappush(lo, -1 * top('hi'))
                heappop(hi)
                balance += 1
            elif balance > 0:
                heappush(hi, top('lo'))
                heappop(lo)
                balance -= 1
            
            while to_remove[top('lo')] != 0:
                to_remove[top('lo')]-=1
                heappop(lo)
            while hi and to_remove[top('hi')] != 0:
                to_remove[top('hi')]-=1
                heappop(hi)
        return res