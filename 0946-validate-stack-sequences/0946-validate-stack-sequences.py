class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        q     = deque(popped)
        
        for num in pushed:
            stack.append(num)
            
            while stack and stack[-1] == q[0]:
                stack.pop()
                q.popleft()
                
                
        return not q
        