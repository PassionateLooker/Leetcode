# 7. Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

class Solution:
    def reverse(self, x):
        if x>0:
            a= int(str(x)[::-1])
        if x<=0:
            a = -1* int(str(x*-1)[::-1])

        mina = -2 ** 31
        maxa = 2 ** 31 - 1
        if a not in range(mina,maxa):
            return 0
        else:
            return a

s=Solution()
print(s.reverse(-139))