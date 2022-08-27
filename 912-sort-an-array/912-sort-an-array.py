class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        def MergeArray(arr,l,y,r):
            ans = [0]* (r-l+1)
            
            i , j , k = l , y+1 , 0
            
            while i <= y and j <= r:
                if arr[i] < arr[j]:
                    ans[k] = arr[i]
                    i += 1
                else:
                    ans[k] = arr[j]
                    j += 1
                    
                k += 1
                
            # adding leftovers values from 1st and 2nd part 
            
            while i <= y:
                ans[k] = arr[i]
                k += 1
                i += 1
                
            while j <= r:
                ans[k] = arr[j]
                k += 1
                j += 1 
                
            # copy sorted values to original array 
            
            counter = 0
            for cp in range(l,r+1):
                arr[cp] = ans[counter]
                counter += 1
                
            return arr
            
            
            
            

        def MergeSort(arr,l,r):

            if l == r:
                return 
            # breaking the array into two equal parts

            mid = (l+r)//2


            MergeSort(arr,l,mid)
            MergeSort(arr,mid+1,r)
            MergeArray(arr,l,mid,r)

            return arr
        
        
        
        return MergeSort(nums,0,len(nums)-1)
        
