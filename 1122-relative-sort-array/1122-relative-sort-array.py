class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1.sort()

        bmap = {}
        for i in arr2:
            if i not in bmap:
                bmap[i] = 1
            else:
                bmap[i] += 1

        amap = {}
        for i in arr1:
            if i not in amap:
                amap[i] = 1
            else:
                amap[i] += 1

        ans = []
        for k in bmap:
            if k in amap:
                while amap[k] > 0:
                    ans.append(k)
                    amap[k] -= 1

        for jk in amap:
            while amap[jk] > 0:
                ans.append(jk)
                amap[jk] -= 1
                
        return ans 