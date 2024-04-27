class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        graph = defaultdict(list)
        for i, c in enumerate(ring):
            graph[c].append(i)
        dp = [min_distance(i, 0, len(ring)) + 1 for i, c in enumerate(ring)]
        for a, b in pairwise(key):
            new_dp = [inf]*len(ring)
            for i, j in product(graph[a], graph[b]):
                new_dp[j] = min(new_dp[j], dp[i] + min_distance(i, j, len(ring)) +  1)
            dp = new_dp
        return min(v for i, v in enumerate(dp) if ring[i] == key[-1])


# return min distance from index i to j in ring with n letters
def min_distance(i, j, n):
    if i > j:
        i, j = j, i
    return min(j - i, i + n - j)