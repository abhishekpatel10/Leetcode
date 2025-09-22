# Last updated: 9/22/2025, 3:48:25 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hash_map = defaultdict(list)
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        curr_max = float('-inf')
        ans = 0
        for key,value in hash_map.items():
            if value > curr_max:
                curr_max = value
                ans =  curr_max
            elif curr_max == value:
                ans += value
        return ans