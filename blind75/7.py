class Solution:
    def reverse(self, x: int) -> int:
        import math
        MAX_INT = 2 ** 31 - 1
        MIN_INT = - 2 ** 31
        # sign = 1
        # if x < 0:
        #     x *= -1
        #     sign = -1

        reverse = 0

        while x != 0:
            print('reverse: ', reverse, MAX_INT, MIN_INT)
            x, digit = math.trunc(x/10), x % 10 if x > 0 else x % -10
            reverse = reverse * 10 + digit
            if reverse > MAX_INT or reverse < MIN_INT:
                return 0

        print('reverse: ', reverse, MAX_INT, MIN_INT)
        return reverse
            
        