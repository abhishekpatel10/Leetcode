# Last updated: 6/8/2025, 11:54:24 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for n in nums:
            if n in hash_map:
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for n,f in hash_map.items():
            freq[f].append(n)
        res=[]
        for i in range(len(freq) - 1 , -1 ,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res