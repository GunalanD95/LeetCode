class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        total = 0
        counter = 0
        idx = len(happiness) - 1
        while k > 0 and idx >= 0:
            cur_val = happiness[idx]
            cur_val -= counter
            if cur_val < 0: break
            total += cur_val
            counter += 1
            idx -=1
            k   -=1
        return total
        