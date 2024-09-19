class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        cache = {}
        if expression in cache:
            return cache[expression]
        res = []
        for i in range(len(expression)):
            if expression[i] in {'+','-','*'}:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] == '+':
                            res.append(l+r)
                        elif expression[i] == '-':
                            res.append(l-r)
                        elif expression[i] == '*':
                            res.append(l*r)
        if not res:
            if expression:
                res.append(int(expression))
        cache[expression] = res 
        return res
        