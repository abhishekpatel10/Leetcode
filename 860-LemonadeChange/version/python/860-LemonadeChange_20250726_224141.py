# Last updated: 7/26/2025, 10:41:41 PM
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        n = len(bills)
        five = tens = 0
        for bill in bills:
            if bill == 5:
                five +=1
            elif bill == 10:
                if five == 0:
                    return False
                five -=1
                tens +=1
            else:
                if tens > 0 and five > 0:
                    tens -=1
                    five -=1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
                

        

