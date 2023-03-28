from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @lru_cache(None)
        def dfs(index = 0, cover = 0):
            '''
                dfs should account for 'coverage', how much a previous purchased
                pass covers the future
            '''
            #print(days, curcost, cover)
            if(index > len(days)-1):
                return 0;
            nextday = days[index]
            if(index > 0 and cover > (nextday- days[index-1])):
                return dfs(index+1, cover- (nextday- days[index-1])); ##prevdays
            else:
                cheapest_val = float('Inf');
                coverage = [1,7,30]
                for c,cost in enumerate(costs):
                    cheapest_val = min(cheapest_val, cost+dfs(index+1, cover = coverage[c]))
                return cheapest_val
        ansr = dfs();
        #print('ansr: ',self.minCost)
        return ansr #self.minCost