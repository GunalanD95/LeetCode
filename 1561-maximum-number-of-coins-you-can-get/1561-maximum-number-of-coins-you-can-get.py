from collections import deque
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        N = len(piles)
        piles.sort()
        q = deque(piles)        
        total_coins = 0
        while q:
            alice , me , bob = q.pop() , q.pop() , q.popleft()
            total_coins += me
        return total_coins