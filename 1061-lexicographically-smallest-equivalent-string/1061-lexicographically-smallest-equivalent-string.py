class Disjoinset():
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
		
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        min_val = min(rootX, rootY)
        max_val = max(rootX, rootY)
        
        if rootX != rootY:
            self.root[max_val] = min_val

    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
        
    
class Solution:
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        get_ascii = lambda ch : ord(ch) - ord('a')
        # merge both s1 and s2
        N = len(s1)
        dsu = Disjoinset(26)
        
        for a,b in zip(s1, s2):
            dsu.union(get_ascii(a), get_ascii(b))
        
        ans = []
        
        for char in baseStr:
            cur_char = get_ascii(char)
            
            index = dsu.find(cur_char)
            nchar = chr(index + ord('a'))
            ans.append(nchar)
            
        return "".join(ans)