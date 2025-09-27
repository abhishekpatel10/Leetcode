# Last updated: 9/27/2025, 1:48:52 AM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        summ = 1
        n = len(ratings)
        l = 1
        peak = 1
        while l < n:
            peak = 1
            if ratings[l] == ratings[l-1]:
                summ += 1
                l += 1
                continue
            peak = 1
            while l < n and ratings[l] > ratings[l-1]:
                summ += peak + 1
                peak += 1
                l += 1
              
            down = 1
            while l < n and ratings[l] < ratings[l-1]:
                summ += down
                down += 1
                l += 1
            if down > 1 and down > peak:
                summ += (down - peak)
        return summ
        
        