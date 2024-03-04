class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        seen = set()
        max_len = 0
        i, j = 0, 0

        while j <= len(s) - 1:
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(s[j])
            max_len = max(len(seen), max_len)
            j += 1

        return max_len
        