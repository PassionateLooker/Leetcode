# 190.
# Reverse Bits

# Reverse bits of a given 32 bits unsigned integer.

# Example
# 1:
#
# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The
# input
# binary
# string
# 00000010100101000001111010011100
# represents
# the

# unsigned
# integer
# 43261596, so
# return 964176192
# which
# its
# binary
# representation is 00111001011110000010100101000000.
class Solution():
    def reverseBits(self,n):
        str="{0:032b}".format(n)
        reversed=str[::-1]
        return int(reversed,2)

s=Solution()
n=0o00111001011110000010100101000000
print(s.reverseBits(n))



# def reverseBits(n):
#     return int(bin(n)[2:].zfill(32)[::-1], 2)
#
# print(reverseBits(11111110000000))
#
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         a = bin(n).replace('0b', "")
#         a = a[::-1]
#         if len(a) != 32:
#             a = a + (32 - len(a)) * '0'
#         return int(a, 2)
# s=Solution()
# print(s.reverseBits(11111110000000))