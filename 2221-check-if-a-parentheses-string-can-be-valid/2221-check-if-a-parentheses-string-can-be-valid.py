class Solution:
    def _validate(self,s ,locked ,sym ):
        main_use = []
        sec_use  = []
        for idx,char in enumerate(s):
            if locked[idx] == '0':
                sec_use.append(idx)
            elif char == sym:
                main_use.append(idx)
            else:
                # if sym is closing , then we need a opening sym for it
                if main_use:
                    main_use.pop()
                elif sec_use:
                    sec_use.pop()
                else:
                    return False
        return True

    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N & 1:
            return False
        return self._validate(s,locked,'(') and  self._validate(s[::-1],locked[::-1],')')        