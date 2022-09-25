class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {}
        for i in range(len(names)):
            d[heights[i]] = names[i]


        heights.sort(reverse=True)
        ans = []

        for i in range(len(heights)):
            ans.append(d[heights[i]])


        return ans 