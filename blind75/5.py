class Solution:
    def longestPalindrome(self, s: str) -> str:

        cur_max = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > cur_max:
                    cur_max = cur_len
                    res = (l, r)
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
                cur_len = r - l + 1
                if cur_len > cur_max:
                    cur_max = cur_len
                    res = (l, r)
                l -= 1
                r += 1
        
        res = s[res[0]:res[1]+1]
        return res

                   