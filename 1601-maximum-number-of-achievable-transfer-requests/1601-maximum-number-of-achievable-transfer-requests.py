class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(idx, count):
            nonlocal max_count

            if idx == len(requests):
                # Check if the net change is zero for all buildings
                if all(balance == 0 for balance in balances):
                    max_count = max(max_count, count)
                return

            from_building, to_building = requests[idx]

            # Simulate the request by decrementing the balance of the 'from_building'
            # and incrementing the balance of the 'to_building'
            balances[from_building] -= 1
            balances[to_building] += 1
            backtrack(idx + 1, count + 1)

            # Undo the request by decrementing the balance of the 'to_building'
            # and incrementing the balance of the 'from_building'
            balances[from_building] += 1
            balances[to_building] -= 1
            backtrack(idx + 1, count)

        max_count = 0
        balances = [0] * n

        backtrack(0, 0)

        return max_count
