#User function Template for python3

def getTriangle( arr, n):
    ans = []
    def sumoftriangle(arr):
        if len(arr) == 1:
            # ans.append(arr[0])
            return 
    
        newarr = []
        prev = arr[0]
        for i in range(1,len(arr)):
            val  = prev + arr[i]
            newarr.append(val)
            prev = arr[i]
         
        sumoftriangle(newarr) 
        if(newarr):
            ans.extend(newarr)
            
    sumoftriangle(arr)
    ans.extend(arr)
    return ans    
    




#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        Triangle = getTriangle(a, n)
        print(*Triangle)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends