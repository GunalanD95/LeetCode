class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        N = len(tiles)
        
        # Generate all unique subsequences
        def substring(indx, cur):
            if cur:  # Exclude empty subsets
                res.add("".join(cur))
            for i in range(indx, N):
                cur.append(tiles[i])
                substring(i + 1, cur)
                cur.pop()

        substring(0, [])
        
        # Generate all unique permutations
        def permutations(nums, indx):
            if indx == len(nums):
                res.add("".join(nums))
                return 
            
            seen = set()  # To avoid duplicate swaps
            for i in range(indx, len(nums)):
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                nums[i], nums[indx] = nums[indx], nums[i]
                permutations(nums[:], indx + 1)  # Use a copy to avoid modifying original list

        for seq in list(res):  # Get permutations of all subsets
            permutations(list(seq), 0)

        return len(res)

