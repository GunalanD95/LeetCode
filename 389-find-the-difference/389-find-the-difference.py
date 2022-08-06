class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        smap =  {}
        tmap =  {}

        for i in range(len(s)):
            if s[i] not in smap:
                smap[s[i]] = 1
            else:
                smap[s[i]] += 1


        for i in range(len(t)):
            if t[i] not in tmap:
                tmap[t[i]] = 1
            else:
                tmap[t[i]] += 1
            
            
            
        for k in tmap:
            if k not in smap:
                return k
            
            else:
                if tmap[k] != smap[k]:
                    return k
        