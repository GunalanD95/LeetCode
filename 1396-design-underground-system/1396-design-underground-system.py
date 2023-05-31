from collections import defaultdict

class UndergroundSystem:
    def __init__(self):
        self.checkin = {}
        self.stationMap = defaultdict(lambda: [0, 0])  # [total_raids, total_time]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.checkin[id]
        dest, t2 = stationName, t

        total_raids, total_time = self.stationMap[(start, dest)]
        total_time += t2 - t1
        total_raids += 1
        self.stationMap[(start, dest)] = [total_raids, total_time]

        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_raids, total_time = self.stationMap[(startStation, endStation)]
        return total_time / total_raids
