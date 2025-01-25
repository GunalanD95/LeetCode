class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        N = len(nums)
        temp = [(num,idx) for idx,num in enumerate(nums)]
        temp.sort()
        grps = []
        cur_grp = []
        prev = float('-inf')
        for num, idx in temp:
            if num > prev + limit:
                grps.extend(sorted(cur_grp))
                cur_grp = [idx]
            else:
                cur_grp.append(idx)
            prev = num
        if cur_grp: grps.extend(sorted(cur_grp))
        ans = [0] * N
        for idx,num in enumerate(grps):
            ans[num] = temp[idx][0] 
        return ans

