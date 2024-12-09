class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [True] * (4 * self.n)  # Allocate space for the segment tree
        self.build(arr, 0, 0, self.n - 1)
        self.arr = arr

    def build(self, arr, node, start, end):
        if start == end:
            # Leaf node: True if the current element has no adjacent element to compare
            self.tree[node] = True
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            # Recursively build the left and right subtrees
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            
            # Combine results for this node:
            # Check if adjacent elements across the left and right children are different
            if mid < end and arr[mid] == arr[mid + 1]:
                self.tree[node] = False
            else:
                self.tree[node] = self.tree[left_child] and self.tree[right_child]

    def query(self, L, R, node, start, end):
        if R < start or L > end:
            # No overlap
            return True  # Neutral value (True for AND operation)
        if L <= start and end <= R:
            # Total overlap
            return self.tree[node]
        # Partial overlap
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_query = self.query(L, R, left_child, start, mid)
        right_query = self.query(L, R, right_child, mid + 1, end)

        # Check for adjacent elements within the range
        if L <= mid and mid + 1 <= R:
            if self.arr[mid] == self.arr[mid + 1]:
                return False
        
        return left_query and right_query
    
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        N = len(nums)
        res = []
        pf = []
        for num in nums:
            if not num & 1:
                pf.append(1)
            else:
                pf.append(2)
        seg_tree = SegmentTree(pf)
        for st,end in queries:
            val = seg_tree.query(st, end, 0, 0, N - 1)
            res.append(val)
        return res
        
        