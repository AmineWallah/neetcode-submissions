from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        need = Counter(s1)
        win = Counter(s2[:k])
        if win == need:
            return True

        for i in range(k, len(s2)):
            win[s2[i]] += 1          # char entering on the right
            win[s2[i - k]] -= 1      # char leaving on the left
            if win[s2[i - k]] == 0:
                del win[s2[i - k]]
            if win == need:
                return True
        return False