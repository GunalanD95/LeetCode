from collections import defaultdict, deque
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # sieve algo to get all prime numebrs from 1 to max(nums)
        n = max(nums)
        if len(nums) == 1:
            return True
        if n == 1:
            return False
        # sieve algo to get primes between 1 to N
        is_prime = [True] * (n+1)
        for i in range(2, n+1):
            if is_prime[i]:
                mul = i
                while(i*mul<=n):
                    is_prime[int(i*mul)] = False
                    mul += 1
        # max prime factor list
        primes = [0] * (n+1)
        for i in range(2, n+1):
            if is_prime[i]:
                for j in range(i, n+1, i):
                    primes[j] = i


        graph = defaultdict(lambda: [])
        for num in nums:
            x = num
            # prime factorization and create graph
            while(x > 1):
                prime = primes[int(x)]
                graph[prime].append(num)
                graph[num].append(prime)
                x = x / prime
        
        # bfs graph
        q = deque()
        visited = set()
        q.append(nums[0])
        visited.add(nums[0])

        while(len(q)>0):
            cur = q.popleft()
            for v in graph[cur]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        
        # check if all nodes are visited
        for num in nums:
            if num not in visited:
                return False
        return True