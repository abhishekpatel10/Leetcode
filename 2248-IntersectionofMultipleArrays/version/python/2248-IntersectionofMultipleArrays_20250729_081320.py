# Last updated: 7/29/2025, 8:13:20 AM
from collections import Counter
from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        b = []
        a = Counter()

        for i in range(len(nums)):
            a.update(set(nums[i]))  # use set to avoid duplicate counts from same list

        for key, value in a.items():
            if value == len(nums):
                b.append(key)  # fixed from `values` to `key`

        return sorted(b)
