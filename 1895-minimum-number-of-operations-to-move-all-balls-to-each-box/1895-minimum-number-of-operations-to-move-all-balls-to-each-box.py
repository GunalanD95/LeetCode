class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res=[0]*len(boxes)

        # Loop Forwards while calculating right-to-left ball movements
        ballsBeingMoved=0
        moves=0
        for i in range(len(boxes)):
            moves+=ballsBeingMoved
            res[i]+=moves
            if boxes[i]=="1":
                ballsBeingMoved+=1
        
        # Loop Backwards while calculating left-to-right ball movements
        ballsBeingMoved=0
        moves=0
        for i in range(len(boxes)-1, -1, -1):
            moves+=ballsBeingMoved
            res[i]+=moves
            if boxes[i]=="1":
                ballsBeingMoved+=1
        return res