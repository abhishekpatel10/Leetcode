# Last updated: 7/29/2025, 8:23:06 AM
class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for x , y, r in circles:
            for x1 in range(x - r , x + r + 1):
                for y1 in range(y - r , y + r + 1):
                    if (x-x1)**2 + (y-y1)**2 <= r**2:
                        points.add((x1,y1))
        return len(points)
         