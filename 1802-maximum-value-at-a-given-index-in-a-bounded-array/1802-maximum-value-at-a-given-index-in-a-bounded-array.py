class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # 要素は正数なので必ず1以上、だから先にn個分の1を引いておく
        maxSum -= n
        ok, ng = 0, maxSum+1
        while abs(ok-ng) > 1:            
            x = (ok+ng)//2
            # indexを真ん中として左と右のそれぞれの長さ
            l, r = index, n-1-index
            
            # [0, index]までの和
            l_sum = (x+x-l)*(l+1)//2
            # [index, n-1]までの和
            r_sum = (x+x-r)*(r+1)//2
            if l > x:
                l_sum = (x+1)*x//2
            if r > x:
                r_sum = (x+1)*x//2

            # xはl_sumとr_sumの両方に含まれて重複しているため引く
            if l_sum+r_sum-x <= maxSum:
                ok = x
            else:
                ng = x

        # 最初に1を引いたので最後に足す                
        return ok+1