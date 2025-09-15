# Last updated: 9/15/2025, 6:26:16 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        n = len(text)
        ss = set(brokenLetters)
        text = text.split(" ")
        n = len(text)
        print(n)
   
        for s in text:
            for ch in s:
                if ch in ss:
                    n -= 1
                    break
        return n

