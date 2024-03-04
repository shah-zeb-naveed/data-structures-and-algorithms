class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """     
            The biggest valid substring we can get is of size maxf + k. So, the larger maxf is, the better. If maxf doesn't change or goes down, our potential best answer doesn't change. We don't need to update maxf in this case.

    On the other hand, if maxf goes up, it means we've found a character in the current window that appears more often than in previous windows. This means we might be able to get a longer valid substring, so we update maxf.

        """

        l = 0
        counter = dict()
        res = 0
        max_f = 0

        for r in range(len(s)):

            counter[s[r]] = 1 + counter.get(s[r], 0)
            max_f = max(max_f, counter.get(s[r]))

            # replaced while with if
            while (r - l + 1) - max_f > k: # max(counter.values())
                counter[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
        