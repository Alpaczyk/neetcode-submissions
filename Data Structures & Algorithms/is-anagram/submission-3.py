class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}

        for i in s:
            counts[i] = counts.get(i, 0) + 1

        for j in t:
            counts[j] = counts.get(j, 0) - 1

        for count in counts.values():
            if count != 0:
                return False

        return True
