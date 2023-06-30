class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        is_land = [[True for i in range(row)] for j in range(col)]
        group = [[-1 for i in range(row)] for j in range(col)]
        c = 2
        for i in range(row):
            for j in range(col):
                if i == 0:
                    group[j][i] = 0
                elif i == row - 1:
                    group[j][i] = 1
                else:
                    group[j][i] = c
                    c += 1

        g = [i for i in range(c)]

        for r, c in cells:
            is_land[c-1][r-1] = False

        def seek(i):
            if i == g[i]:
                return i
            else:
                assert 0 <= g[i] < i
                return seek(g[i])

        def join(i, j):
            si = seek(i)
            sj = seek(j)
            g[i]=g[j]=g[si]=g[sj]=min(si, sj)
            
        for i in range(col):
            for j in range(row):
                if is_land[i][j]:
                    for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                        if i + di >= col or j + dj >= row or i + di < 0 or j + dj < 0 or not is_land[di+i][dj+j]:
                            continue
                        else:
                            join(group[i][j], group[i+di][j+dj])

        day = len(cells)
        while day:
            if seek(1) == 0:
                return day
            i, j = cells[day-1][1] - 1, cells[day-1][0] - 1
            day -= 1
            is_land[i][j] = True
            for di, dj in [(1,0), (0,1), (-1,0), (0,-1)]:
                if i + di >= col or j + dj >= row or i + di < 0 or j + dj < 0 or not is_land[di+i][dj+j]:
                    continue
                else:
                    join(group[i][j], group[i+di][j+dj])

        return 0