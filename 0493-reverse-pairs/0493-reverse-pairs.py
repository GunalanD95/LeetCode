def merge_arr(x,y,z,arr):
    count = 0
    j = y + 1  

    for i in range(x, y + 1):
        while j <= z and arr[i] > 2 * arr[j]:
            j += 1
        count += (j - (y + 1))
        
    ans = [0] * (z-x+1)
    i , j , k = x , y+1 , 0
    
    while i <= y and j <= z:
        if arr[i] <= arr[j]:
            ans[k] = arr[i]
            i += 1
        else:
            ans[k] = arr[j]
            j += 1
        k += 1
    while i <= y:
        ans[k] = arr[i]
        k += 1
        i += 1
    while j <= z:
        ans[k] = arr[j]
        k += 1
        j += 1
    counter = 0
    for cp in range(x,z+1):
        arr[cp] = ans[counter]
        counter += 1
    return count 

def mergesort(l,r,arr):
    if l >= r:
        return 0
    mid = (l+r)//2
    a = mergesort(l,mid,arr)
    b = mergesort(mid+1,r,arr)
    c = merge_arr(l,mid,r,arr)
    return a+b+c

def mergecount(arr):
    return mergesort(0,len(arr)-1,arr)

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return mergecount(nums)