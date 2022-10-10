#User function Template for python3

#Function to reverse the queue.
import queue 
def rev(q):
    #add code here
    stack = []
    
    while q.qsize() != 0:
        ele = q.get()
        stack.append(ele)
     
    while stack:
        ele = stack.pop()
        q.put(ele)
        
    return q


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from queue import Queue
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().split()))
        q=Queue(maxsize=n+1)
        for j in a:
            q.put(j)
        q=rev(q)
        for i in range(0,n):
            print(q.get(),end=" ")
        print()
# } Driver Code Ends