class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d  = {}
        d1 = {}

        if len(pattern) != len(s.split()):
            return False

        for i,val in enumerate(s.split()):
            if val not in d:
                d[val] = pattern[i]
            else:
                if d[val] != pattern[i]:
                    return False

        s = s.split()
        for i,val in enumerate(pattern):
            if val not in d1:
                d1[val] = s[i]
            else:
                if d1[val] !=  s[i]:
                    return False


        return True          