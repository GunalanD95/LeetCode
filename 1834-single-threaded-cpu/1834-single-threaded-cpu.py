import heapq as hq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N         = len(tasks)
        
        for idx in range(len(tasks)):
            tasks[idx].append(idx)

        tasks.sort(key= lambda x: x[0])      # sort by enque time 

        res , min_heap = [] , []

        cur_tasks = 0
        time     = 0
        time     += tasks[0][0]              # initial time 


        while min_heap or cur_tasks < len(tasks):
            while cur_tasks < len(tasks) and time >= tasks[cur_tasks][0]:
                hq.heappush(min_heap , [tasks[cur_tasks][1],tasks[cur_tasks][2]])
                cur_tasks += 1

            if not min_heap:
                time = tasks[cur_tasks][0]
            else:
                tym , idx = hq.heappop(min_heap)
                time += tym
                res.append(idx)

        return res