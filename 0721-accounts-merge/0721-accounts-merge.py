from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        N = len(accounts)
        
        email_to_ids = defaultdict(set)
        idx_to_name = {}
        
        # Build the mappings
        for idx, account in enumerate(accounts):
            name = account[0]
            idx_to_name[idx] = name
            for email in account[1:]:
                email_to_ids[email].add(idx)
        
        visited = set()
        res = []
        
        def dfs(idx, cur_emails):
            visited.add(idx)
            # Access the emails from the current account
            for email in accounts[idx][1:]:
                cur_emails.add(email)
                for account_id in email_to_ids[email]:
                    if account_id not in visited:
                        dfs(account_id, cur_emails)
        
        # Iterate through each account and perform DFS
        for idx in range(N):
            if idx not in visited:
                cur_emails = set()
                dfs(idx, cur_emails)
                if cur_emails:
                    merged_account = [idx_to_name[idx]] + sorted(cur_emails)
                    res.append(merged_account)

        return res