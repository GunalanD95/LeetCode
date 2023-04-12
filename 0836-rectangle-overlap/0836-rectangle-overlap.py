class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rleft1 = rec1[0]
        
        
        # y
        rleft2 = rec1[1]
        
        rright1 = rec1[2]
        
        # y
        rright2 = rec1[3]

        vleft1 = rec2[0]
        
        # y
        vleft2 = rec2[1]
        
        vright1 = rec2[2]
        
        
        # y
        vright2 = rec2[3]
        
        
        if not ( rleft1 < vright1 and vleft1 < rright1 ):
            return False
        if not ( rleft2 < vright2 and vleft2 < rright2 ):
            return False        
        return True
        
        
        
        