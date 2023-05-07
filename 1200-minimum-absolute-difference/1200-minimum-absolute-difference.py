class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        min_diff = float('inf')
        
        arr.sort()
        
        N = len(arr)
        
        hmap = defaultdict(list)
        
        for i in range(1,N):
            cur_diff = abs(arr[i-1]-arr[i])
            min_diff = min(min_diff,cur_diff)
            
            hmap[cur_diff].append([arr[i-1],arr[i]])
            
            
        return hmap[min_diff]