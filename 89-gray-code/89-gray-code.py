class Solution:
    def grayCode(self, n: int) -> List[int]:
        def graycode(n,ans):
            if n == 0:
                return 
            if n == 1:
                ans.append(0)
                ans.append(1)
            graycode(n-1,ans)

            msb = 1<< n-1
            if n > 1:
                s = len(ans) - 1
                while s >= 0:
                    ans.append(ans[s]+msb)
                    s -= 1
            return ans


        return graycode(n,[])
        