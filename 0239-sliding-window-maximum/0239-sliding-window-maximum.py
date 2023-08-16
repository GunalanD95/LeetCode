from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        A = nums
        N = len(nums)
        q = deque()

        N = len(A)
        ans = []
        for i in range(k):
            cur_ele = A[i]
            while q and cur_ele > q[-1]: 
                q.pop()
            q.append(cur_ele) 
            
        for i in range(N-k):
            out_gn = A[i]
            if out_gn == q[0]:
                ele = q.popleft()
                ans.append(ele)
            else:
                ans.append(q[0])

            in_cmg = A[i+k]
            while q and in_cmg > q[-1]:
                q.pop()

            q.append(in_cmg)

        if q: 
            ans.append(q.popleft())   
        
        return ans 