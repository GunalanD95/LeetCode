from typing import List
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def can_assign(k):
            task_list = tasks[:k]
            worker_list = SortedList(workers[-k:])
            pills_left = pills

            for i in reversed(range(k)):
                task = task_list[i]

                # Case 1: Can we assign without pill?
                if worker_list and worker_list[-1] >= task:
                    worker_list.pop()  # use strongest worker
                else:
                    # Find the first worker who can do the task WITH a pill
                    idx = worker_list.bisect_left(task - strength)
                    if idx == len(worker_list) or pills_left == 0:
                        return False
                    worker_list.pop(idx)
                    pills_left -= 1

            return True

        low, high = 0, min(len(tasks), len(workers))
        ans = 0

        while low <= high:
            mid = (low + high) // 2
            if can_assign(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans
