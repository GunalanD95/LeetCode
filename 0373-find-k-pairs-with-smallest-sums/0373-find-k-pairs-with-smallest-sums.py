import heapq as hq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        N , M = len(nums1) , len(nums2)
        
        min_heap = []
        
        N , M = len(nums1) , len(nums2)
        seen = set()
        for idx in range(M): 
            cur_sum = nums1[0] + nums2[idx]
            hq.heappush(min_heap,(cur_sum,0,idx))
            seen.add((0,idx))
            
        res = []
        while min_heap and k > 0:
            cur_sum , idx1 , idx2 = hq.heappop(min_heap)
            
            res.append([nums1[idx1],nums2[idx2]])
            
            if idx1+1 < N and idx2 < M and (idx1+1,idx2) not in seen:
                newSum = nums1[idx1+1]  + nums2[idx2]
                hq.heappush(min_heap,(newSum,idx1+1,idx2))
                seen.add((idx1+1,idx2))
                
            if idx1 < N and idx2+1 < M and (idx1,idx2+1) not in seen:
                newSum = nums1[idx1]  + nums2[idx2+1]
                hq.heappush(min_heap,(newSum,idx1,idx2+1))
                seen.add((idx1,idx2+1))
                
            k -= 1      
        return res
        