class TrieNode:
    def __init__(self,char):
        self.char  = char
        self.edges = {}
        self.isEnd = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        
    def insert(self,word)-> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                newNode = TrieNode(char)
                cur_node.edges[char] = newNode
            cur_node = cur_node.edges[char]
        cur_node.isEnd = True
        
    def search(self,word)-> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                return False
            cur_node = cur_node.edges[char]
        return cur_node.isEnd == True
        
        
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        '''insert all wordDict in Trie'''
        for word in wordDict:
            trie.insert(word)
    
        def word_break_helper(s, trie, curr_words, result):
            if not s:
                result.append(" ".join(curr_words))
                return
            
            for i in range(1, len(s)+1):
                prefix = s[:i]
                if trie.search(prefix):
                    curr_words.append(prefix)
                    word_break_helper(s[i:], trie, curr_words, result)
                    curr_words.pop()
        
        result = []
        word_break_helper(s, trie, [], result)
        return result        
        