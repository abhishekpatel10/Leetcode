# Last updated: 6/8/2025, 11:54:15 AM
class Solution:
    def frequencySort(self, s: str) -> str:
        h1 = Counter(s)
        buckets = defaultdict(list)

        for char, cnt in h1.items():
            buckets[cnt].append(char)
        res = ""
        for i in range(len(s),0,-1):
            for c in buckets[i]:
                res += c * i
        return res
            

        