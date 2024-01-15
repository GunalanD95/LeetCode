from collections import defaultdict 

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        WinMap  = defaultdict(int)
        LostMap = defaultdict(int)
        
        
        won_all  = set()
        lost_one = set()
        
        for winner,loser in matches:
            WinMap[winner] += 1
            LostMap[loser] += 1
            
            if winner not in won_all and LostMap[winner] == 0:
                won_all.add(winner)
            if loser in won_all:
                won_all.remove(loser)
                
            if loser not in lost_one and LostMap[loser]== 1:
                lost_one.add(loser)
            elif loser in lost_one and LostMap[loser] > 0:
                lost_one.remove(loser)
                
        won_all = sorted(won_all)
        lost_one = sorted(lost_one)
        
        return [won_all,lost_one]