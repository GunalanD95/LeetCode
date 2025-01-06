class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        ans = [0] * N

        for idx in range(N):
            cur = 0
            for jdx in range(N):
                if idx == jdx:
                    continue
                if boxes[jdx] == '1':
                    diff = abs(idx - jdx)
                    cur += diff
            ans[idx] = cur
        return ans
        