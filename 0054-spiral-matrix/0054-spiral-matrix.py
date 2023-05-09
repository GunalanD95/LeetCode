class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        A =  matrix
        rows = len(A)
        cols = len(A[0])

        top = 0
        dn = len(A) - 1
        left  = 0
        right = cols - 1
        dir = 'r'
        res = []
        while top <= dn and left<= right:
            if dir == 'r':
                for i in range(left,right+1):
                    res.append(A[top][i])
                top += 1
                dir = 'd'

            elif dir == 'd':
                s = top
                e = dn
                while s <=e:
                    res.append(A[s][right])
                    s+=1
                right -=1
                dir = 'l'

            elif dir == 'l':
                s = right
                e = left
                while s >= e:
                    res.append(A[dn][s])
                    s -= 1
                dn -=1
                dir = 't'

            elif dir == 't':
                s = dn
                e = top
                while s >= e:
                    res.append(A[s][left])
                    s -= 1
                left += 1
                dir = 'r'
                
        return res