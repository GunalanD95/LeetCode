class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key = lambda x: -x[1])
        
        units = 0
        
        for box in boxTypes:
            if truckSize > 0:
                if truckSize >= box[0]:
                    units += (box[0] * box[1])
                    truckSize -= box[0]
                else:
                    units += (truckSize * box[1])
                    return units 
                
            else:
                break
                
                
        return units 