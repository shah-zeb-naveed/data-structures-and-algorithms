class Solution:

    def valid(self, c):
        return c.isalpha() or c.isnumeric()

    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not self.valid(s[i]):
                i += 1
            while j > i and not self.valid(s[j]):
                j -= 1
            
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1
            
        return True
            
        