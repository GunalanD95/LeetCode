class Solution:
    def countUnguarded(self, rows: int, cols: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        walls_set = set(map(tuple, walls))
        guards_set = set(map(tuple, guards))
        guarded = set()  

        def go_fully(r, c, dr, dc):
            r += dr
            c += dc
            while 0 <= r < rows and 0 <= c < cols:
                if (r, c) in walls_set or (r, c) in guards_set:
                    break  
                guarded.add((r, c))  
                r += dr
                c += dc

        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]  

        for r, c in guards:
            for dr, dc in directions:
                go_fully(r, c, dr, dc)

        total_cells = rows * cols
        blocked_cells = len(walls_set) + len(guards_set)
        guarded_cells = len(guarded)

        return total_cells - blocked_cells - guarded_cells
