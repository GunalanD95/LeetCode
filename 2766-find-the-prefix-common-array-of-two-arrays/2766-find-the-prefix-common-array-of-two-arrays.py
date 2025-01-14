from collections import defaultdict
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        both = set()
        a_map = defaultdict(int)
        b_map = defaultdict(int)
        res   = []
        for num1,num2 in zip(A,B):
            a_map[num1] += 1
            b_map[num2] += 1
            if num1 in b_map:
                both.add(num1)
            if num2 in a_map:
                both.add(num2)
            res.append(len(both))
        return res
