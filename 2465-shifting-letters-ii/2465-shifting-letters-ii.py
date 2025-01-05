class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        N = len(s)
        diff = [0] * N

        for l,r,direction in shifts:
            # inc by 1
            if direction == 1:
                diff[l] += 1
                if r+1 < N:
                    diff[r+1] -= 1
            else:
                # dec by 1
                diff[l] -= 1
                if r+1 < N:
                    diff[r+1] += 1

        prefix_sum = 0
        s = list(s)
        for i, val in enumerate(diff):
            prefix_sum += val
            shift = prefix_sum % 26  # Normalize the shift to be within [0, 25]
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))
            s[i] = new_char

        return "".join(s)