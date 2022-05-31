class Solution:
    def isPalindrome(self, x: int) -> bool:     
        rev_x = list(str(x))
        def swap(A):
            N = len(A)
            s =  0
            e = N - 1
            while s <= e:
                temp = A[s]
                A[s] = A[e]
                A[e] = temp
                
                s += 1
                e -= 1
            return A
        
        k = swap(rev_x)
        k2 = ''.join(k)
        if str(x) == k2:
            return True
        else:
            return False