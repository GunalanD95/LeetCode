class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        map1 = defaultdict(int)
        rowmap = defaultdict(set)
        colmap = defaultdict(set)
        rows , cols = len(mat) , len(mat[0])
        for row in range(rows):
            for col in range(cols):
                colmap[col].add(mat[row][col])
                rowmap[row].add(mat[row][col])
                map1[mat[row][col]] = (row,col)
        idx = 0
        while idx < len(arr):
            row , col = map1[arr[idx]]
            rowmap[row].remove(arr[idx])
            colmap[col].remove(arr[idx])
            if len(rowmap[row]) == 0 or len(colmap[col])  == 0:
                return idx
            idx += 1
        return 0