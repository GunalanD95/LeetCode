class Solution:
    def compare_string(self,string1,string2):
        diff  = 0

        for idx in range(self.N):
            if string1[idx] != string2[idx]:
                diff += 1
                if diff > 1:
                    return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.N = len(beginWord)
        graph  = collections.defaultdict(list)
        wordList.append(beginWord)

        for i in range(len(wordList)):
            for j in range(i+1,len(wordList)):
                if self.compare_string(wordList[i],wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        q = deque()
        q.append((beginWord,1))

        visited = set()
        visited.add(beginWord)

        min_len = 0
        while q:
            cur_word , cur_len = q.popleft()
            if cur_word == endWord:
                return cur_len
            for child_word in graph[cur_word]:
                if child_word not in visited:
                    visited.add(child_word) 
                    q.append((child_word,cur_len+1))
        return min_len
