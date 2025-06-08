# Last updated: 6/8/2025, 11:52:26 AM
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        for i in range(len(number) - 1):
            if number[i] == digit and number[i + 1] > digit:
                return number[:i] + number[i+1:]
        last_index = number.rfind(digit)
        return number[:last_index] + number[last_index + 1:]