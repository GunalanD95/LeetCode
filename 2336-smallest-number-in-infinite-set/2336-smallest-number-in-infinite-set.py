class SmallestInfiniteSet:

    def __init__(self):
        temp = list(range(1,1001))
        self.set = set(temp)

    def popSmallest(self) -> int:
        smallest = min(self.set)
        self.set.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
