class Node:
    def __init__(self,char:str,is_end=False):
        self.char = char
        self.values = {}
        self.is_end = is_end
        
class Trie:
    def __init__(self):
        self.root_node = Node(None)
        
    def add_word(self,word: str) -> None:
        cur_node = self.root_node
        for char in word:
            if char not in cur_node.values():
                newnode = Node(char)
                cur_node[char] = newnode
            cur_node = cur_node[char]
        cur_node.is_end = True
        
    def search_word(self,word: str) -> bool:
        cur_node = self.root_node
        for char in word:
            if char not in cur_node.values():
                return False
            cur_node = cur_node[char]
        return cur_node.end
    
    def find_prefix(self,word: str) -> bool:
        cur_node = self.root_node
        for char in word:
            if char not in cur_node.values():
                return False
            cur_node = cur_node[char]
        return True
    
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict =  set(wordDict)
        N = len(s)
        
        @cache
        def find_all(indx):
            if indx >= N:
                return True
            ans = False
            for idx in range(indx,N):
                if s[indx:idx+1] in wordDict:
                    ans |= find_all(idx+1)
            return ans
        
        
        return find_all(0)
        
        