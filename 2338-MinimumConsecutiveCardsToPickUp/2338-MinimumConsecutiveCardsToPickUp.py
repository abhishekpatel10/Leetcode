# Last updated: 6/8/2025, 11:52:25 AM
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}  
        ans = float('inf')  

        for i, card in enumerate(cards):
            
            if card in last_seen:
                ans = min(ans, i - last_seen[card] + 1)
            
            last_seen[card] = i

        
        return -1 if ans == float('inf') else ans
            

