class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        xerocount = arr.count(0)
        N = len(arr)

        for k in range(N-1, -1, -1):

            if k + xerocount < N:
                arr[k + xerocount] = arr[k]


            if arr[k] == 0:
                xerocount -= 1
                if k + xerocount < N:
                    arr[k+xerocount] = 0
