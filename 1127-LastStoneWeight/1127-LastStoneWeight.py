# Last updated: 6/8/2025, 11:53:02 AM
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            if largest != next_largest:
                heapq.heappush(stones,largest - next_largest)
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0