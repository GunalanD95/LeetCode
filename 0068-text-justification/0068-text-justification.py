class Solution:
    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        def output_line(words):
            if len(words) == 1:
                return words[0] + ' ' * (max_width - len(words[0]))
            
            spaces, remaining_spaces = divmod(max_width - sum(len(word) for word in words), len(words) - 1)
            ans = []
            for i in range(len(words) - 1):
                ans.append(words[i])
                ans.append(' ' * (spaces + (i < remaining_spaces)))
            ans.append(words[-1])
            return "".join(ans)
        
        ans = []
        current_line = []
        for word in words:
            # Check if the current word can fit in the current line
            if len(word) + sum(len(w) for w in current_line) + len(current_line) <= max_width:
                current_line.append(word)
            else:
                ans.append(output_line(current_line))
                current_line = [word]
        
        # Handle the last line
        if current_line:
            ans.append(output_line([" ".join(current_line)]))
        
        return ans