class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        N , M = len(s) , len(goal)
        
        if N != M:
            return False
        
        
        
        for st in range(N):
            for end in range(M):
                if s[st] == goal[end]:
                    i = st
                    j = end
                    
                    count = 0
                    while count < N:
                        print(count,s[i],goal[j])
                        if s[i] == goal[j]:
                            i += 1
                            j += 1
                        else:
                            break
                            
                        count += 1
                        i %= N
                        j %= M
                        
                        
                    if count == N:
                        return True
                    
                    
        return False