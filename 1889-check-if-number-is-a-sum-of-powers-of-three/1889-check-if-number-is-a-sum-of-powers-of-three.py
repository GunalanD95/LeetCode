class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            print("n",n,n%3)
            if n % 3 == 2:
                return False
            n //= 3

        return True
            