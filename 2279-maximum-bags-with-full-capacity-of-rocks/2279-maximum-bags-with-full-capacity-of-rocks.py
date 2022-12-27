class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        N = len(capacity)
        max_bags = 0
        for idx in range(N):
            capacity[idx] = abs(capacity[idx] - rocks[idx])

        capacity.sort()

        for indx in range(N):
            if additionalRocks >= capacity[indx]:
                max_bags += 1
                additionalRocks -= capacity[indx]


        return max_bags



