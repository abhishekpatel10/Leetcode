# Last updated: 6/8/2025, 11:52:51 AM
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        
        max_sum = sum(cardPoints[:k])
        curr_sum = max_sum
        
        
        for i in range(1, k + 1):
            curr_sum = curr_sum - cardPoints[k - i] + cardPoints[-i]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
            
            
            
