class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        N = len(words)
        words_set = set(words)
        res = []

        for word in words:
            if word not in words_set:
                continue
            for i in range(len(word)):
                cur_string = ''
                for j in range(i,len(word)):
                    cur_string += word[j]
                    if cur_string in words_set and cur_string != word:
                        res.append(cur_string)
                        words_set.remove(cur_string)
        return res


        