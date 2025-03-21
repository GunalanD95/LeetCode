class Solution:
    def check_palindrome(l,r,string) -> bool:
        while l <= r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        return True
    def isPalindrome(self, s: str) -> bool:
        string = []
        for char in s:
            if char.isalnum():
                string.append(char.lower())

        print("string",string)
        return string == string[::-1]
        