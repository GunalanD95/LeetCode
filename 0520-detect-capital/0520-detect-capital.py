class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        N = len(word)
        
        capi = False
        count = 0
        cap   = 0
        if word[0].isupper(): 
            capi = True
            cap  += 1
        
        for i in range(N):
            if not capi:
                if word[i].islower():
                    count += 1
            else:
                if i > 0:
                    if word[i].islower():
                        count += 1
                    else:
                        cap   += 1
                        
        print("capi",capi,cap,count,N)
        if not capi:
            if count == N:
                return True
            else:
                return False
        else:
            if word[0].isupper() and word[-1].isupper():
                print("no")
                if cap == N:
                    return True
                else:
                    return False
            else:
                print("yes")
                if cap == 1:
                    return True
                else:
                    return False
            
        
        