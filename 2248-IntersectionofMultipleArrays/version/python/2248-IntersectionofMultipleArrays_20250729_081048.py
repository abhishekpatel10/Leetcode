# Last updated: 7/29/2025, 8:10:48 AM
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hash_map = Counter()
        print(hash_map)
        for num in nums:
            for v in num:
                hash_map[v] += 1
        print(hash_map)
        ans = []
        for u ,v in hash_map.items():
            if hash_map[u] == len(nums):
                ans.append(u)
        return sorted(ans)
            
        


        