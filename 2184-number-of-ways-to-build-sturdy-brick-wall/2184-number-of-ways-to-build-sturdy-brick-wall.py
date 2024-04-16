class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        combos = []
        def dfs(combo, w):
            if w == width:
                combos.append(tuple(combo[:-1]))
                return
            for b in bricks:
                if w + b <= width:
                    combo.append(w + b)
                    dfs(combo, w + b)
                    combo.pop()
        dfs([], 0)
        print("combos",combos)
        
        d = collections.defaultdict(set)
        
        for i in range(len(combos)):
            for j in range(i, len(combos)):
                if not set(combos[i]) & set(combos[j]):
                    d[i].add(j)
                    d[j].add(i)      
                    
                    
        print('d',d)
        cash = defaultdict()
        def findCombos(h, comID):
            if h == 1:
                return 1
            if (h, comID) in cash:
                return cash[(h, comID)]
            s = 0
            for nextID in d[comID]:
                s += findCombos(h-1, nextID) 
            cash[(h, comID)] = s % (10**9+7) 
            return s
        
        return sum(findCombos(height, c) for c in range(len(combos))) % (10**9+7)         