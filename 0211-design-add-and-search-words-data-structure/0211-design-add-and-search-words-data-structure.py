class TrieNode:
    def __init__(self,char):
        self.char  = char
        self.edges = {}
        self.isEnd = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)
        

    def addWord(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = TrieNode(char)
            cur_node = cur_node.edges[char]
        cur_node.isEnd = True
                
    def search(self, word: str) -> bool:
        return self.dfs(self.root,word,0)
    
    def dfs(self,node,word,indx):
        if indx >= len(word):
            return node.isEnd

        cur_char = word[indx]
        if cur_char == '.':
            for key in node.edges:
                if self.dfs(node.edges[key],word,indx+1):
                    return True
            return False
        else:
            if cur_char not in node.edges:
                return False
            return self.dfs(node.edges[cur_char],word,indx+1)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)