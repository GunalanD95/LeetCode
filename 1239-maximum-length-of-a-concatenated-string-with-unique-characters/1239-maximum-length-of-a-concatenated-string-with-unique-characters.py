class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        N = len(arr)
        ans = 0
        
        def findmaxsubseq(indx,cur_arr):
            nonlocal ans
            if indx >= N:
                string = "".join(cur_arr)
                if len(string) == len(set(string)):
                    ans = max(ans,len(string))
                return
            cur_string = arr[indx]
            # dont take 
            findmaxsubseq(indx+1,cur_arr)
            # take it
            cur_arr.append(cur_string)
            findmaxsubseq(indx+1,cur_arr)
            cur_arr.pop()
            
            
        findmaxsubseq(0,[])
        return ans