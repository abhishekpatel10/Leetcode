# Last updated: 6/8/2025, 11:54:44 AM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        n = len(nums)
        for i in range(n):
            heapq.heappush(pq,-nums[i])
        f = k - 1
        while f > 0:
            heapq.heappop(pq)
            f-=1
        return -pq[0]