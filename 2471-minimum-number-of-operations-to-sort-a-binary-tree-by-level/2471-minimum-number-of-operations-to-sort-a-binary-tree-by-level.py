from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        if not root: return
        
        q = deque()
        q.append(root)
        total = 0
        while q:
            lvl = []
            for idx in range(len(q)):
                cur_node = q.popleft()
                lvl.append(cur_node.val)
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            
            hashmap = {val:idx for idx,val in enumerate(lvl)}
            sorted_lvl = sorted(lvl)
            for idx in range(len(lvl)):
                cur_num = lvl[idx]
                tar_num = sorted_lvl[idx]
                
                if cur_num != tar_num:
                    total += 1
                    lvl[idx] , lvl[hashmap[tar_num]] = lvl[hashmap[tar_num]] , lvl[idx]
                    hashmap[cur_num] = hashmap[tar_num]
            
            
        return total