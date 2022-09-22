class Solution:
    def reverseWords(self, s: str) -> str:
        st , end = 0 , 0
        s = list(s)
        N = len(s)
        while st < len(s) and end < len(s):
            if s[end] == ' ':
                stt  , endd = st , end - 1

                while stt <= endd:
                    temp = s[stt]
                    s[stt] = s[endd]
                    s[endd] = temp
                    stt += 1
                    endd -= 1


                st = end + 1
            elif end == N-1:
                stt  , endd = st , end 

                while stt <= endd:
                    temp = s[stt]
                    s[stt] = s[endd]
                    s[endd] = temp
                    stt += 1
                    endd -= 1        

            end += 1


        return "".join(s)       