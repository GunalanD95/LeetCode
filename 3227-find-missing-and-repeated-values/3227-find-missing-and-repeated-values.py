class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        max_range = n*n

        seen = {i:0 for i in range(1,max_range+1)}

        ans = []
        for row in grid:
            for val  in row:
                if val in seen:
                    del seen[val]
                else:
                    ans.append(val)

        ans = ans + list(seen.keys())
        return ans