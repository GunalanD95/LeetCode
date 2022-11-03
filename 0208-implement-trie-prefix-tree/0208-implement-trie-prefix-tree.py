class Trie_Node:
    def __init__(self,char):
        self.val     = char
        self.edges   = {}
        self.isEnd   = 0
    
class Trie:

    def __init__(self):
        self.root = Trie_Node(None)
        

    def insert(self, word: str) -> None:
        cur_node = self.root
        
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Trie_Node(char)
                
            cur_node = cur_node.edges[char]
            
        cur_node.isEnd += 1
            
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        
        for char in word:
            if char not in cur_node.edges:
                return False
            cur_node = cur_node.edges[char]
            
        if cur_node.isEnd > 0:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        
        for char in prefix:
            if char not in cur_node.edges:
                return False
            cur_node = cur_node.edges[char]
            
        return True         
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)