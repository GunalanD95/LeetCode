class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def has_common_subarray(k: int) -> bool:
            # Hash all subarrays of length k in nums1
            hash_set = set()
            current_hash = 0
            base, mod = 101, 2**63 - 1
            
            # Compute hash for the first k-length subarray in nums1
            for i in range(k):
                current_hash = (current_hash * base + nums1[i]) % mod
            hash_set.add(current_hash)
            
            # Sliding window to compute hashes for remaining subarrays in nums1
            base_k = pow(base, k, mod)  # Base^k % mod
            for i in range(k, len(nums1)):
                current_hash = (current_hash * base - nums1[i - k] * base_k + nums1[i]) % mod
                hash_set.add(current_hash)
            
            # Check subarrays in nums2
            current_hash = 0
            for i in range(k):
                current_hash = (current_hash * base + nums2[i]) % mod
            
            if current_hash in hash_set:
                return True
            
            for i in range(k, len(nums2)):
                current_hash = (current_hash * base - nums2[i - k] * base_k + nums2[i]) % mod
                if current_hash in hash_set:
                    return True
            
            return False
        
        # Binary search for the maximum length
        low, high = 0, min(len(nums1), len(nums2))
        max_len = 0
        
        while low <= high:
            mid = (low + high) // 2
            if has_common_subarray(mid):
                max_len = mid
                low = mid + 1  # Try for a longer subarray
            else:
                high = mid - 1  # Try for a shorter subarray
        
        return max_len
