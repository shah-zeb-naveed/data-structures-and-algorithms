class Solution:
    def reverseBits(self, n: int) -> int:

        # converting to str/bin and then appending 0 is too many
        # passes. Use >> operator solution

        # res = 0
        # for i in range(32):
        #     bit = (n >> i) & 1
        #     res = res | (bit << (31 - i))

        # can also just use mod to extract last bit
        res = 0
        for i in range(32):
            n, bit = n // 2, n % 2
            res = res << 1
            res += (bit)

        return res
        