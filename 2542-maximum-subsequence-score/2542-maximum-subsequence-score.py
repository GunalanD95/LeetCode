from heapq import heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 1: return max(v1 * v2 for (v1, v2) in zip(nums1, nums2))
        n = len(nums1)
        if k == n: return sum(nums1) * min(nums2)
        sorted_nums1 = sorted([(v, i) for i, v in enumerate(nums1)], key=lambda x: -x[0])
        s, hq = 0, []
        for v, i in sorted_nums1[:k]:
            s += v
            heappush(hq, (nums2[i], i))
        ans = hq[0][0] * s
        for v, i in sorted_nums1[k:]:
            s += v - nums1[heappop(hq)[1]]
            heappush(hq, (nums2[i], i))
            ans = max(ans, s * hq[0][0])
        return ans