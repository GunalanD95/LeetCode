from collections import defaultdict

class Node:
    def __init__(self,is_end=False):
        self.edges = {}
        self.is_end = is_end

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        N = len(folder)
        
        root_node = Node()
        
        for path in folder:
            cur_node = root_node
            folders  = path.split("/")
            
            
            for foldername in folders:
                if foldername == '':
                    continue
                    
                if foldername not in cur_node.edges:
                    cur_node.edges[foldername] = Node()
                    
                cur_node = cur_node.edges[foldername]
                
            cur_node.is_end = True
            
        res = []
        
        for path in folder:
            cur_node = root_node
            folders  = path.split('/')
            
            is_sub_folder = False
            
            
            for i,foldername in enumerate(folders):
                if foldername == '':
                    continue
                    
                next_node = cur_node.edges[foldername]
                
                if next_node.is_end and i != len(folders)-1:
                    is_sub_folder = True
                    break
                
                cur_node = next_node
                
            if not is_sub_folder:
                res.append(path)
            
            
        
        return res