class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate_all_pairs(curr,open_count,close_count):
            if len(curr) == 2*n:
                res.append("".join(curr))
                return
            
            if open_count < n:
                curr.append('(')
                generate_all_pairs(curr,open_count+1,close_count)
                curr.pop()
                
            if close_count < open_count:
                curr.append(')')
                generate_all_pairs(curr,open_count,close_count+1)
                curr.pop()
        
        generate_all_pairs([],0,0)
        return res