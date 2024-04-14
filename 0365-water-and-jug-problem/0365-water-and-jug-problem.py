class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        stack = [(0, 0)]
        seen = set()

        while stack:
            cur_x, cur_y = stack.pop()
            if (cur_x, cur_y) in seen:
                continue

            seen.add((cur_x, cur_y))

            if cur_x + cur_y == target:
                return True

            # Filling x bucket
            stack.append((x, cur_y))
            # Filling y bucket
            stack.append((cur_x, y))
            # Emptying x bucket
            stack.append((0, cur_y))
            # Emptying y bucket
            stack.append((cur_x, 0))
            # Pouring from x to y
            stack.append((max(0, cur_x - (y - cur_y)), min(y, cur_y + cur_x)))
            # Pouring from y to x
            stack.append((min(x, cur_x + cur_y), max(0, cur_y - (x - cur_x))))

        return False
