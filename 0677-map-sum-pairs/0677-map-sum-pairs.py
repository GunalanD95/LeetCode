class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.dic = {}
        

    def insert(self, key: str, val: int) -> None:
        delta = val - self.dic.get(key, 0)
        self.dic[key] = val
        cur = self.root
        cur.freq += delta
        
        for char in key:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
            cur.freq += delta
        

    def sum(self, prefix: str) -> int:
        cur = self.root
        for symbol in prefix:
            if symbol not in cur.children:
                return 0
            cur = cur.children[symbol]
        return cur.freq
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)