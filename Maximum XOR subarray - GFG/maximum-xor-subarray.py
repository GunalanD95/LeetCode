#User function Template for python3
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
    def maxSubarrayXOR (self, n, arr):
        # code here
        ans = float('-inf')
        A = [None]*(len(arr)+1)
        A[0] = 0
        for i in range(1,len(arr)+1):
            A[i] = A[i-1] ^ arr[i-1]
            
        max_len = len(bin(max(A))) - 2             # get max length of all numbers' binary
        trie = Trie(max_len)
        for num in A:  
            trie.insert(num)

        ''' getting max prefix pair '''
        max_val = 0
        for num in A:
            cur_node = trie.root
            for shift in range(max_len,-1,-1):
                val = 1 if num & (1 << shift) else 0
                val_dash = 1 - val
                if val_dash in cur_node.edges:
                    cur_node = cur_node.edges[val_dash]
                else:
                    cur_node = cur_node.edges[val]

            max_val = max(max_val,num ^ cur_node.val)

        return max_val

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
    
        ob = Solution()
        print(ob.maxSubarrayXOR(N,arr))
        

# } Driver Code Ends