class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        max_length = 0
        left = 0

        for right in range(len(s)):
            curr = s[right]

            if curr in seen and seen[curr] >= left:
                left = seen[curr] + 1
            
            seen[curr] = right

            max_length = max(max_length, right - left + 1)
        
        return max_length
        