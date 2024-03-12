class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}

        for idx,num in enumerate(nums):
            if num in hmap:
                diff = abs(idx - hmap[num])
                if diff <=k:
                    return True

            hmap[num] = idx

        return False
        