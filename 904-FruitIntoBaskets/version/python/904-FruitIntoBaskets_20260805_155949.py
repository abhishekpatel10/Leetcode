# Last updated: 8/5/2026, 3:59:49 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        hash_map = {}
4        ans = 0
5        l = 0
6        for i in range(len(fruits)):
7            hash_map[fruits[i]] = hash_map.get(fruits[i],0) + 1
8            while len(hash_map) > 2:
9                hash_map[fruits[l]] -= 1
10                if hash_map[fruits[l]] == 0:
11                    del hash_map[fruits[l]]
12                l += 1
13            ans = max(ans, i - l+ 1)
14        return ans
15
16