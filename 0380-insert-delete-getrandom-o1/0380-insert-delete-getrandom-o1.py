import random 

class RandomizedSet:

    def __init__(self):
        self._set = set()
        
    def insert(self, val: int) -> bool:
        if val not in self._set:
            self._set.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        cur = list(self._set)
        return random.choice(cur)