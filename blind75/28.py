class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return - 1

        # apply pmp algo
        # create lps array
        lps = [0] * len(needle)
        pre = 0
        for i in range(1, len(needle)):
            while pre > 0 and needle[i] != needle[pre]:
                pre = lps[pre-1]
            
            if needle[i] == needle[pre]:
                pre += 1
                lps[i] = pre

        n = 0
        for h in range(len(haystack)):
            while n > 0 and needle[n] != haystack[h]:
                n = lps[n - 1]

            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1

        return - 1

        # start = 0

        # while start <= len(haystack) - len(needle):

        #     h, n = start, 0
        #     while n < len(needle) and needle[n] == haystack[h]:
        #         h += 1
        #         n += 1

        #     if n == len(needle):
        #         return start
            
        #     start += 1

        # return -1

        