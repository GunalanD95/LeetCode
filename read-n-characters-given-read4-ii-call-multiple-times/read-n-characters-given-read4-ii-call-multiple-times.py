# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:
'''
ref : https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/discuss/4866526/Python3-Straightforward-solution-with-extensive-explanations-and-code-comments
'''
from collections import deque

class Solution:
    def __init__(self):
        self._read_but_not_used = deque([])
        self._buf4 = [None] * 4
        
        
    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while len(self._read_but_not_used) > 0 and  i < n:
            c = self._read_but_not_used.popleft()
            buf[i] = c 
            i += 1
            
        if i == n:
            return i
        
        # Now, iteratively call read4 until we have enough chars to return, or until we reach EOF.
        while i < n:
            read4(self._buf4)
            
            i_b = 0
            while i_b < len(self._buf4) and self._buf4[i_b] is not None and i < n:
                buf[i] = self._buf4[i_b]
                i += 1
                self._buf4[i_b] = None
                i_b += 1
                
            if i == 0 or i_b < len(self._buf4):
                while i_b < len(self._buf4) and self._buf4[i_b] is not None:
                    self._read_but_not_used.append(self._buf4[i_b])
                    self._buf4[i_b] = None
                    i_b += 1
                return i
        return i
                    
                
        