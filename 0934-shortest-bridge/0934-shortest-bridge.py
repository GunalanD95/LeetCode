class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        n = len(A)
        # get one point from any island
        def getFirst():
            for i, row in enumerate(A):
                for j, point in enumerate(row):
                    if point == 1:
                        return (i,j)
        islandA = []
        boundaries = []
        # DFS first to find the boundary of first island
        stack = [getFirst()]
        while len(stack) > 0:
            i, j = stack.pop()
            # label it
            A[i][j] = -1
            islandA.append((i, j))
            isBound = False
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n:
                    if A[x][y] == 0:
                        boundaries.append((i,j))
                    elif A[x][y] == 1:
                        stack.append((x,y))
                    
        
        # all the points on island A is stored in islandA now
        # BFS to expend it
        step = 0
        while boundaries:
            new = []
            for i, j in boundaries:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            boundaries = new