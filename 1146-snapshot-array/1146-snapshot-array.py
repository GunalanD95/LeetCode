class SnapshotArray:
    def __init__(self, length: int):
        # consider each index as a key -> versions
        self.arr = [[[-1, 0]] for _ in range(length)] # (snap_id,value)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.arr[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        cur_arr = self.arr[index]
        
        low, high = 0, len(cur_arr) - 1
        
        # extreme right since we need the latest version
        while low <= high:
            mid = (low + high) // 2
            if cur_arr[mid][0] <= snap_id:
                low = mid + 1
            else:
                high = mid - 1
        
        return cur_arr[high][1]
