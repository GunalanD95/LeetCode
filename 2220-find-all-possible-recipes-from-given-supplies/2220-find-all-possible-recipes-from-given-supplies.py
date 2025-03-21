import heapq as hq

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        N = len(recipes)
        supplies = set(supplies)

        indegree = [0] * (N)
        ingrt_map = defaultdict(set)

        for idx,recipe in enumerate(recipes):
            for ingrts in ingredients[idx]:
                if ingrts not in supplies:
                    indegree[idx] += 1
                    ingrt_map[ingrts].add((idx,recipe))

        min_heap = []
        for idx in range(N):
            if indegree[idx] == 0:
                hq.heappush(min_heap,idx)
        res = []
        while min_heap:
            recipe_indx = hq.heappop(min_heap)
            res.append(recipes[recipe_indx])

            for p_indx,p_receipe in ingrt_map[recipes[recipe_indx]]:
                indegree[p_indx] -= 1
                if indegree[p_indx] == 0:
                    hq.heappush(min_heap,p_indx)
            
        return res