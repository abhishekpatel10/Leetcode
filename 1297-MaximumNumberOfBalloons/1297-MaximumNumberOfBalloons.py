# Last updated: 6/8/2025, 11:52:58 AM
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        h = defaultdict(int)
        a = 'balloon'

        for i in text:
            if i in a:
                h[i] += 1
        
        if any(c not in h for c in a):
            return 0 
        else:
            return min(h['b'],h['a'],h['l']//2,h['o']//2,h['n'])
        

        

        