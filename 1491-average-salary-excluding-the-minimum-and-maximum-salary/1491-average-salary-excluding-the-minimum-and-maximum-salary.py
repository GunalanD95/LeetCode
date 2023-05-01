class Solution:
    def average(self, salary: List[int]) -> float:        
        total = sum(salary)
        total -= min(salary)
        total -= max(salary)
        total = total / (len(salary) - 2)

        formatted_num = "{:.5f}".format(round(total, 5))

        return float(formatted_num)        