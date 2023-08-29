class Solution:
    def bestClosingTime(self, customers: str) -> int:
        N = len(customers)
        closed = []
        opened = []
        
        for num in customers:
            if num == 'Y':
                closed.append(1)
                opened.append(0)
            else:
                closed.append(0)
                opened.append(1)
                
        for i in range(1, N):
            closed[i] = closed[i-1] + closed[i]
            opened[i] = opened[i-1] + opened[i]
        
        min_penalty = float('inf')
        min_hour = -1
        
        for i in range(N + 1):
            if i == 0:
                left_sum = 0
                right_sum = closed[N-1]
            elif i == N:
                right_sum = 0
                left_sum = opened[N-1]
            else:
                left_sum = opened[i-1]
                right_sum = closed[N-1] - closed[i-1]
            
            penalty = left_sum + right_sum
            if penalty < min_penalty:
                min_penalty = penalty
                min_hour = i
        
        return min_hour
