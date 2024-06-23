class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        
        # On3 --> On2 --> On
        maxLen, i = 0, 0
        minQueue, maxQueue = collections.deque([]), collections.deque([])
        for j in range(len(nums)):
            while minQueue and minQueue[-1] > nums[j]:
                minQueue.pop()
            minQueue.append(nums[j])
            while maxQueue and maxQueue[-1] < nums[j]:
                maxQueue.pop()
            maxQueue.append(nums[j])
            
            if maxQueue[0] - minQueue[0] <= limit:
                maxLen = max(maxLen, j-i+1)
            else:
                if maxQueue[0] == nums[i]:
                    maxQueue.popleft()
                if minQueue[0] == nums[i]:
                    minQueue.popleft()
                i += 1
        return maxLen