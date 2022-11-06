class Trie_Node:
    def __init__(self):
        self.edges = {}
        self.val = 0                                  # end value 

class Trie:
    def __init__(self,n):
        self.root    = Trie_Node()
        self.max_len = n
        
    def insert(self,cur_val):
        cur_node = self.root 
        for j in range(self.max_len,-1,-1):
            val = 1 if cur_val & (1 << j) else 0
            if val not in cur_node.edges:
                cur_node.edges[val] = Trie_Node()
            cur_node = cur_node.edges[val]
        cur_node.val = cur_val

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        '''inserting and building prefix binary tree'''
        max_len = len(bin(max(nums))) - 2             # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in nums:  
            trie.insert(num)

        ''' getting max prefix pair '''
        max_val = 0
        for num in nums:
            cur_node = trie.root
            for shift in range(max_len,-1,-1):
                val = 1 if num & (1 << shift) else 0
                val_dash =  1 - val
                if val_dash in cur_node.edges:
                    # print("yes",val_dash,num)
                    cur_node = cur_node.edges[val_dash]
                else:
                    # print("no",val,num)
                    cur_node = cur_node.edges[val]

            # print("max_val",max_val,num,cur_node.val)
            max_val = max(max_val,num ^ cur_node.val)

        return max_val








        