class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def inverpairs(arr,l,mid,end):
            ptr1 = l
            ptr2 = mid + 1
            count = 0
            while ptr1<= mid and ptr2 <= end:
                if arr[ptr1] > 2 * arr[ptr2]:
                    count += mid - ptr1 + 1
                    ptr2 += 1
                else:
                    ptr1 += 1

            return count



        def RevArr(arr,l,mid,end):
            i = l 
            j = mid+1

            ans = [0] * (end-l+1)
            k = 0
            while i <= mid and j <= end:
                if arr[i] <= arr[j]:
                    ans[k] = arr[i]
                    i += 1
                else:
                    ans[k] = arr[j]
                    j += 1  

                k += 1


            while i <= mid:
                ans[k] = arr[i]
                i += 1 
                k += 1

            while j <= end: 
                ans[k] = arr[j]
                j += 1 
                k += 1 

            counter = 0
            for indx in range(l,end+1):
                arr[indx] = ans[counter]
                counter += 1

            return arr 


        def RevSort(arr,l,r):
            if l == r:
                return 0

            mid = (l+r) // 2 

            A = RevSort(arr,l,mid)
            B = RevSort(arr,mid+1,r)
            AB = inverpairs(arr,l,mid,r)
            RevArr(arr,l,mid,r)

            ans = A + B + AB
            return ans
        
        
        return RevSort(nums,0,len(nums)-1)