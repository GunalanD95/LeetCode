class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            cur_email = []
            last_found_symbol = None
            for char in email:
                if last_found_symbol != '@' and char == '.':
                    continue
                elif char == '@':
                    last_found_symbol = '@'
                elif last_found_symbol != '@' and char == '+':
                    last_found_symbol = '+'
                
                if last_found_symbol != '+':
                    cur_email.append(char)
                
            seen.add("".join(cur_email))
        
        return len(seen)
        