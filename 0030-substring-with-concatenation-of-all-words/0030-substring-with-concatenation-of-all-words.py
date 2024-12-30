from collections import Counter, defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        total_len = word_len * len(words)
        words_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = defaultdict(int)
            count = 0  # Count of valid words in the current window
            
            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len
                
                if word in words_count:
                    current_count[word] += 1
                    count += 1
                    
                    # If a word is over-counted, shrink the window from the left
                    while current_count[word] > words_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    # If all words match, add the starting index
                    if count == len(words):
                        result.append(left)
                else:
                    # Reset window
                    current_count.clear()
                    count = 0
                    left = right

        return result
