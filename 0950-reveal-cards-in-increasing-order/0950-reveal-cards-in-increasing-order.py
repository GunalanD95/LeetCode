from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        N = len(deck)
        deck.sort()
        queue = deque(range(N))
        result = [0] * N
        
        for card in deck:
            result[queue.popleft()] = card
            if queue:
                queue.append(queue.popleft())
        
        return result
