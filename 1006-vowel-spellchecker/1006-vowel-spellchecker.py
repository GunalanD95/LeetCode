from collections import defaultdict
from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # Step 1: Preprocess wordlist
        wordlist_set = set(wordlist)
        
        # Dictionary to store lowercase word mappings (for exact and capitalized matches)
        word_mapper = defaultdict(list)
        # Dictionary to store words grouped by their vowel pattern
        vowel_pattern_mapper = defaultdict(list)
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        def get_vowel_pattern(word: str) -> str:
            # Replace vowels with a placeholder to generate a pattern
            return ''.join(c if c not in vowels else 'X' for c in word.lower())
        
        for word in wordlist:
            # For exact matching, lowercase version as the key
            word_mapper[word.lower()].append(word)
            
            # For vowel error matching, store by vowel pattern
            vowel_pattern_mapper[get_vowel_pattern(word)].append(word)
        
        # Step 2: Function to check capitalized form
        def check_capitalized(word: str):
            low_word = word.lower()
            if low_word in word_mapper:
                return word_mapper[low_word][0]
            return None
        
        # Step 3: Function to check vowel error
        def check_vowel_error(word: str):
            pattern = get_vowel_pattern(word)
            if pattern in vowel_pattern_mapper:
                return vowel_pattern_mapper[pattern][0]
            return None

        # Step 4: Process each query
        result = []
        
        for query in queries:
            # Step 4a: First, check for an exact match
            if query in wordlist_set:
                result.append(query)
                continue
            
            # Step 4b: Check for capitalized match
            capitalized_match = check_capitalized(query)
            if capitalized_match:
                result.append(capitalized_match)
                continue
            
            # Step 4c: Check for vowel error match
            vowel_match = check_vowel_error(query)
            if vowel_match:
                result.append(vowel_match)
                continue
            
            # Step 4d: If no match, append empty string
            result.append("")
        
        return result
