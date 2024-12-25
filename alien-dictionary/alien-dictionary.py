from collections import defaultdict, Counter, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indeg = Counter({c:0 for word  in words for c in word})
        
        for first_word,second_word in zip(words,words[1:]):
            for c,d in zip(first_word,second_word):
                if c != d:
                    if d not in graph[c]:
                        graph[c].add(d)
                        indeg[d] += 1
                    break
            else:
                if len(second_word) < len(first_word):
                    return ""
                
        
        output = []
        q = deque([c for c in indeg if indeg[c] == 0])
        
        while q:
            c = q.popleft()
            output.append(c)
            for d in graph[c]:
                indeg[d] -= 1
                if indeg[d] == 0:
                    q.append(d)

        if len(output) < len(indeg):
            return ""        
        
        
        return "".join(output)