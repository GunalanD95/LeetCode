from collections import defaultdict

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        N = len(folder)
        
        folder.sort(key=lambda x: len(x))
        
        folderMap = defaultdict(int)
        
        
        for subfolder in folder:
            cur_char = subfolder.split('/')
            root_folder = ''
            flag = True
            for char in cur_char:
                if char != '':
                    root_folder += '/'+char
                if root_folder in folderMap:
                    flag = False
                    break
            if root_folder not in folderMap:
                folderMap[root_folder] += 1       
        return list(folderMap.keys())