class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indeg = [0] * (n+1)
        graph = defaultdict(list)
        
        for pre,nxt in relations:
            graph[pre].append(nxt)
            indeg[nxt] += 1
            
        q = deque()
        for course in range(1,n+1):
            count = indeg[course]
            if count == 0:
                q.append(course)
                
        
        min_sems = 0
        total    = n
        
        visited  = set()
        while q:
            for _ in range(len(q)):
                cur_course = q.popleft()
                
                
                if cur_course in visited:
                    continue
                    
                total -= 1
                for child_course in graph[cur_course]:
                    indeg[child_course] -= 1
                    if indeg[child_course] == 0:
                        q.append(child_course)
                        
            min_sems += 1        
        
        return min_sems if total == 0 else -1
        