from collections import defaultdict

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal:
            # Check if there are any repeated characters in s
            counts = defaultdict(int)
            for char in s:
                counts[char] += 1
            for count in counts.values():
                if count >= 2:
                    return True
            return False
        
        nonmatching = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                nonmatching.append((s[i], goal[i]))
        
        if len(nonmatching) != 2:
            return False
        
        return nonmatching[0] == nonmatching[1][::-1]
