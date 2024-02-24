class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
            stack = set()
            graph = defaultdict(list)
            for x, y, _ in grp: 
                graph[x].append(y)
                graph[y].append(x)
                if x in can: stack.add(x)
                if y in can: stack.add(y)
                    
            stack = list(stack)
            while stack: 
                x = stack.pop()
                for y in graph[x]: 
                    if y not in can: 
                        can.add(y)
                        stack.append(y)
        return can