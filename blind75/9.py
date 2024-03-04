class Solution:
    def isPalindrome(self, x: int) -> bool:

        # sign = 1 if x >= 0 else -1
        # if x < 0: x * -1

        if x < 0:
            return False

        # x = str(x)
        # return x == x[::-1]

        digits = []

        while x != 0:
            print(x)
            x, digit = x // 10, x % 10
            digits.append(digit)

        l, r = 0, len(digits) - 1

        while l < r:
            if digits[l] != digits[r]:
                return False

            l += 1
            r -= 1
            
        return True
