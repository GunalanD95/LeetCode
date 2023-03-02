class Solution:
    def compress(self, chars: List[str]) -> int:
        r_index = 0

        # outer loop
        while r_index < len(chars):

            # count at least 1 for first char we look at
            count = 1

            # inner loop - how far can we go
            while r_index + 1 < len(chars) and chars[r_index] == chars[r_index + 1]:
                count += 1
                 # we know the next char is same so lets delete it and look at the next after it without having to update r_index
                del chars[r_index + 1]

            # now handle if count is numerical digit like 12 a characters,  "a", "1", "2"
            if count > 1:
                for char in str(count):
                    chars.insert(r_index + 1, char)
                    r_index += 1

            r_index += 1

        return len(chars)           