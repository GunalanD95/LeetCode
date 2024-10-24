import heapq as hq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        stations.append((target,float('inf')))
        
        refuels = 0
        max_heap = []
        prev_station = 0
        
        for location,fuel in stations:
            startFuel -= (location - prev_station)
            
            
            while max_heap and  startFuel < 0:
                startFuel += -hq.heappop(max_heap)
                refuels += 1

                
            if startFuel < 0:
                return -1
            
        
            hq.heappush(max_heap,-fuel)
            prev_station = location
            
            
        return refuels
        