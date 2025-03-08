class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        N = len(blocks)
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count += 1

        min_count = count
        left  = 0
        right = k

        while right < N:
            min_count = min(min_count,count)
            if blocks[left] == 'W':
                count -= 1

            if blocks[right] == 'W':
                count += 1
            min_count = min(min_count,count)
            left  += 1
            right += 1


        return min_count