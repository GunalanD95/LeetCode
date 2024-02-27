class TrieNode:
    def __init__(self,char):
        self.val       = char
        self.edges     = {}
        self.pf_counter      = 0 

class Trie:
    def __init__(self):
        self.root_node = TrieNode('DummyNode')
        
    def insert(self,word):
        root_node = self.root_node
        for char in word:
            if char not in root_node.edges:
                root_node.edges[char] = TrieNode(char)
            root_node.edges[char].pf_counter += 1  
            root_node = root_node.edges[char]
            
            
    def search(self,prefix,total_words):
        root_node = self.root_node
        cur_char   = ''
        
        for char in prefix:
            if char not in root_node.edges:
                return cur_char
            else:
                if root_node.edges[char].pf_counter != total_words:
                    return cur_char
            cur_char += char
            root_node = root_node.edges[char]
        return cur_char
            
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        
        for word in strs:
            trie.insert(word)
            
        return trie.search(strs[0],len(strs))
        
        
        