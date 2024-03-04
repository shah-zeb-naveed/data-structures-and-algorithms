class Solution:
    def myAtoi(self, s: str) -> int:
        MAX_INT, MIN_INT = 2 ** 31 - 1, - 2 ** 31
        i, state, sign, num = 0, 0, 1, 0 
        
        while i < len(s):
            c = s[i]

            if state == 0:
                if c == ' ':
                    pass
                    i += 1
                
                elif c in ['+', '-']:
                    sign = 1 if c == '+' else -1
                    state = 1
                    i += 1

                elif c.isdigit():
                    state = 2
                
                else:
                    return 0

            elif state == 1:
                if not c.isdigit():
                    return 0
                state = 2

            elif state == 2:
                if not c.isdigit():
                    break

                num = num * 10 + int(c)

                if sign == 1:
                    if num > MAX_INT: return MAX_INT
                else:
                    if (num * sign) < MIN_INT: return MIN_INT

                i += 1

        return num * sign