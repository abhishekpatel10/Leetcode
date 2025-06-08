# Last updated: 6/8/2025, 11:54:30 AM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paper_counts = [0] * (n +1)

        for c in citations:
            paper_counts[min(c,n)] +=1
        
        h = n 
        paper = paper_counts[n]
        while paper < h:
            h -= 1
            paper += paper_counts[h]
        return h