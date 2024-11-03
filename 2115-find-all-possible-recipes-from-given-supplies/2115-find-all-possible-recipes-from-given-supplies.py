from collections import defaultdict
import heapq as hq

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        res = []
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for idx,recipe in enumerate(recipes):
            dependent_recipes = []
            count = 0
            flag  = False
            for ingredient in ingredients[idx]:
                # two cases 
                # 1: it can be normal ingredient ie not another recipe
                # 2: it can be another recipe , so we need to make that to have this
                # if all the recipe-ingredients are normal and present in supplies
                if ingredient in recipes:
                    dependent_recipes.append(ingredient)
                elif ingredient in supplies:
                    count += 1
                elif ingredient not in supplies:
                    flag = True
                    break
            # if a ingredient not an recipe and not avaiable in supplies
            if flag:
                continue
            # all the recipes are avaiable in supplies only
            if count == len(ingredients[idx]):
                indegree[recipe] = 0
                continue
            for depend_recipe in dependent_recipes:
                graph[depend_recipe].append(recipe)
            if dependent_recipes:
                indegree[recipe] = len(ingredients[idx]) - count # depends on x recipes

        q = deque()
        for recipe,count in indegree.items():
            if count == 0:
                q.append(recipe)

        while q:
            cur_recipe = q.popleft()
            
            res.append(cur_recipe)
            for dependent in graph[cur_recipe]:
                indegree[dependent] -= 1
                
                # got all ingrendent recepies
                if indegree[dependent] == 0:
                    q.append(dependent)

        return res