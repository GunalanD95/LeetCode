class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        max_val = float('inf')

        left_max   = 0

        cur_cost   = coins
        for num in costs:
            if num <= cur_cost:
                left_max += 1
                cur_cost -= num

            print(num,cur_cost)

        return left_max


        