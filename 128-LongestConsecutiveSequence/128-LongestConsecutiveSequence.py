# Last updated: 6/8/2025, 11:55:07 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        s = set(nums)  # Convert nums to a set for O(1) lookups
        max_len = 0

        for num in s:  # Iterate over the set, not the list
            # Start a new sequence only if it's the start of a sequence
            if num - 1 not in s:
                current_num = num
                length = 1
                
                while current_num + 1 in s:
                    current_num += 1
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len