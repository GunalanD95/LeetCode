from collections import deque

class Solution:
    def openLock(self, deadends, target):
        # Concept - You need to think this as a graph and once that is visualized, the problem just
        # Translates to finding a shortest path from source ('0000') to destination (target)
        # that also incorporates the constraints (deadends)
        
        # For constant Lookups and avoiding TLE
        deadends = set(deadends)
        # For checking visited nodes
        seen = set()
        # Start point
        seen.add('0000')
        # Put it in queue
        q = collections.deque(['0000'])
        # Our final result aka shortest path
        minSteps = 0
        
        while q:
            size = len(q)
            
            for i in range(size):
                lockPos = q.popleft()
                # We should continue in case of deadends
                if lockPos in deadends:
                    continue
                # If you have reached the target in thuis process, return from here only 
                if lockPos == target:
                    return minSteps
                
                temp = lockPos
                # Else make the other 2 strings(nodes) that are possible by adding or subtracting 1
                for i in range(4):
                    curPos = int(temp[i])
                    s1 = temp[0:i] + ('0' if curPos == 9 else str((curPos + 1)%10))  + temp[i+1:]
                    s2 = temp[0:i] + ('9' if curPos == 0 else str((curPos - 1)%10)) + temp[i+1:]
                    
                    # Only add this into queue once you verify the constraints
                    if s1 not in seen and s1 not in deadends:
                        seen.add(s1)
                        q.append(s1)
                    
                    if s2 not in seen and s2 not in deadends:
                        seen.add(s2)
                        q.append(s2)
            # Add 1 to steps to go to the next level as we were not able to find target in this level            
            minSteps += 1
        return -1