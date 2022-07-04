class Solution:
    def grayCode(self, n: int) -> List[int]:
        A = n
        def getbinary(number):
            if number == 0:
                return 0
            smallans = getbinary(number // 2)
            return number % 2 + 10 * smallans
        
        result  = []
        for i in range(1<<A):
            val = '0' + str(getbinary(i))
            res = val[0]
            
            for j in range(1,len(val)):
                if val[j] == val[j-1]:
                    res = res + '0'
                else:
                    res = res + '1'
            result.append(int(res,2))


        return(result)