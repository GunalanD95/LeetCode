class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        
        Acount = 0
        Bcount = 0
        
        for i in range(1,n-1):
            if colors[i-1] == colors[i] and colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    Acount += 1
                else:
                    Bcount += 1
        return Acount > Bcount
        