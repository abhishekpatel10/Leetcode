# Last updated: 6/8/2025, 11:52:48 AM
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stc = []

        for i in range(1,target[-1] + 1):
            if i not in target and i < target[-1]:
                stc.append("Push")
                stc.append("Pop")
            else:
                stc.append("Push")
        return stc
            
