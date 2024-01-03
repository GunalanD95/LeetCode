class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        
        
        ans = 0
        last_row_val = 0
        
        for row in bank:
            devices = 0
            for cell in row:
                if cell == '1':
                    devices += 1
            
            if devices > 0:
                ans += devices * last_row_val
                last_row_val = devices
            
            
        return ans