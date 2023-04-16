class Solution:
    def dp(self,col, idxTarget):
        if (col, idxTarget) in self.memo:
            return self.memo[(col, idxTarget)]
        if idxTarget == self.lenTarget:  # Formed a valid target
            return 1
        if col == self.cols:  # Explored all columns but didnt create target
            return 0
        char = self.target[idxTarget]
        ans=0
        ans += self.dp(col + 1, idxTarget + 1) * self.counter[col][char] if self.counter[col][char] > 0 else 0 # If cound char at col, build rest of Target starting char+1 using remaining cols col+1
        ans += self.dp(col + 1, idxTarget)  # Skip col_th column and try to make Target using columns col + 1 to end
        ans %= self.MOD
        self.memo[(col, idxTarget)]=ans
        return ans
    def numWays(self, words: List[str], target: str) -> int:
        self.memo=dict()
        self.target=target
        self.MOD = 10 ** 9 + 7
        self.cols, self.lenTarget = len(words[0]), len(target)
        self.counter = [collections.Counter() for _ in range(self.cols)] # a counter for every column
        for word in words: #counter hash
            for idx, char in enumerate(word):
                self.counter[idx][char] += 1  # Count the number of character `char` at index `idx`
        return self.dp(0, 0)