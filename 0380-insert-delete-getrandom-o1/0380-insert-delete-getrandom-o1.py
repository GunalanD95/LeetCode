import random 

class RandomizedSet:

    def __init__(self):
        self._mapper    = {}
        self._values    = []
        
    def insert(self, val: int) -> bool:
        if val in self._mapper:
            return False
        
        self._values.append(val)
        get_len = len(self._values) - 1
        self._mapper[val] = get_len  
        
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self._mapper:
            return False
        
        index = self._mapper[val]
        last_val = self._values[-1]

        self._values[index] = last_val
        self._mapper[last_val] = index

        self._values.pop()
        del self._mapper[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self._values)