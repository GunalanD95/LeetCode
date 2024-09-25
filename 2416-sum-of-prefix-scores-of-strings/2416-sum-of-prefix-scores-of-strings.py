class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0  # Counts how many times this prefix appears during insertion

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
            cur_node.prefix_count += 1  # Increment prefix count as we move through the Trie

    def getPrefixScores(self, word: str) -> int:
        cur_node = self.root
        cur_sum = 0
        for char in word:
            cur_node = cur_node.children[char]
            cur_sum += cur_node.prefix_count
        return cur_sum

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        
        # Insert all words into the Trie
        for word in words:
            trie.insert(word)
        
        # Calculate the prefix scores for each word by summing the prefix counts
        result = []
        for word in words:
            result.append(trie.getPrefixScores(word))
        
        return result
