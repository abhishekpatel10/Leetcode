# Last updated: 9/4/2025, 2:27:47 PM
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        one_dis = abs(x-z)
        two_dis = abs(y-z)
        if one_dis < two_dis:
            return 1
        elif one_dis == two_dis:
            return 0
        else:
            return 2