#User function Template for python3

class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        # code here
        ans = []
        visited = [False] * (V)

        def dfs(cur_node):
            # if not cur_node:
            #     return 
    
            ans.append(cur_node)
            
            visited[cur_node] = True 
            nodes         = len(adj[cur_node])
    
            for child in range(nodes):
                if not visited[ adj[cur_node][child] ]:
                    dfs(adj[cur_node][child])


        for node in range(V):
            if not visited[node]:
                dfs(node)
        
        return ans 
        
        


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends