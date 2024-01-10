from collections import deque , defaultdict

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        graph = defaultdict(list)
        
        q = deque()
        q.append(root)
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()                
                if cur_node.left:
                    graph[cur_node.val].append(cur_node.left.val)
                    graph[cur_node.left.val].append(cur_node.val)
                    q.append(cur_node.left)
                if cur_node.right:
                    graph[cur_node.val].append(cur_node.right.val)   
                    graph[cur_node.right.val].append(cur_node.val)
                    q.append(cur_node.right)
                    
        
        q = deque()
        q.append(start) # start node
        
        total_minutes = -1
        seen = set()
        seen.add(start)
        
        while q:
            for _ in range(len(q)):
                cur_node = q.popleft()
                                
                for child in graph[cur_node]:
                    if child not in seen:
                        seen.add(child)
                        q.append(child)

            total_minutes += 1
            
        return total_minutes
        
        
                    
                    
        