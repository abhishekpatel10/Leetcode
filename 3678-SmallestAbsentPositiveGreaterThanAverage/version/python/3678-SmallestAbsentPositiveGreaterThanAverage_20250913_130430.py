# Last updated: 9/13/2025, 1:04:30 PM
class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        count=Counter()
        discarded=0
        l=0
        n=len(arrivals)
        seen=[True]*n
        for r in range(n):
            count[arrivals[r]]+=1
            if(r-l==w):
                if(seen[l]):
                    count[arrivals[l]]-=1
                l+=1
            if(count[arrivals[r]]>m):
                discarded+=1
                count[arrivals[r]]-=1
                seen[r]=False   
        return discarded

            
            