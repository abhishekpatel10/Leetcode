# Last updated: 6/8/2025, 11:53:59 AM
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stc = []
        for num in operations:
            if num == 'C' and stc:
                stc.pop()
            elif num == 'D'and stc:
                a = stc[-1]
                b = stc.append(a*2)
            elif num == "+":
                stc.append(stc[-1]+stc[-2])
            else:
                stc.append(int(num))

        print('>>>',stc)
        return sum(stc)