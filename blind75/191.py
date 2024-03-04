class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bits = 0
        while n:
            # sol1
            #n, current_bit = n // 2,int(n % 2 > 0)

            # # sol2
            # current_bit = 1 & n
            # n = n >> 1

            # n_bits += current_bit

            # sol3
            n = n & (n - 1)
            n_bits += 1

        return n_bits
