class Trie_Node:
    def __init__(self,char):
        self.val       = char
        self.edges     = {}
        self.isEnd     = False 
        
class Trie:
    def __init__(self):
        self.root = Trie_Node(None)
        
    def insert(self, word: str) -> None:
        '''Inserts word into the trie'''
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                cur_node.edges[char] = Trie_Node(char)
                
            cur_node = cur_node.edges[char] 
        cur_node.isEnd = True
        
    def search(self, word: str) -> bool:
        '''Checks word into the trie'''
        cur_node = self.root
        for char in word:
            if char not in cur_node.edges:
                return False
            else:
                cur_node = cur_node.edges[char]
                
        return cur_node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        count = 0
        for char in prefix:
            if char in cur_node.edges:
                cur_node = cur_node.edges[char]
            else:
                return count
            count += 1
        return count

class Solution:

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        max_len = 0
        
        
        trie = Trie()
        
        for num in arr1:
            val = str(num)
            trie.insert(val)
        
        for num2 in arr2:
            val = str(num2)
            max_len = max(max_len,trie.startsWith(val))
 
        return max_len
        