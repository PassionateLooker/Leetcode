# 1323.
# Maximum
# 69
# Number
#
# Given
# a
# positive
# integer
# num
# consisting
# only
# of
# digits
# 6 and 9.
#
# Return
# the
# maximum
# number
# you
# can
# get
# by
# changing
# at
# most
# one
# digit(6
# becomes
# 9, and 9
# becomes
# 6).
#
# Example
# 1:
#
# Input: num = 9669
# Output: 9969
# Explanation:
# Changing
# the
# first
# digit
# results in 6669.
# Changing
# the
# second
# digit
# results in 9969.
# Changing
# the
# third
# digit
# results in 9699.
# Changing
# the
# fourth
# digit
# results in 9666.
# The
# maximum
# number is 9969.


# class Solution:
#     def maximum69Number (self, num) :
#         s=str(num)
#         i=s.find('6')
#         if i==-1:
#             return num
#         else:
#             return s[:i]+'9'+s[i+1:]
#
# # or
# res = str(num)
# for i in range(len(res)):
#     if res[i] == "6":
#         return int(res[:i]+"9"+res[i+1:])
#     return num
#
# # or
#
# s=str(n)
#         for i in range(len(s)):
#             if s[i]=='6':return int('9'*(i+1)+s[i+1:])
#         return n
class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        for i in range(len(s)):
            if s[i]=='6':
                print(int('9'*(i+1)+s[i+1:]))
        return num
s=Solution()
print(s.maximum69Number(9669))

# or
class Solution:
    def maximum69Number(self, num: int) -> int:
        string = str(num)
        for i in range(len(string)):
            if string[i] == '6':
                new_string = string.replace('6', '9', 1)
                return new_string

        return string


# or
return int(str(num).replace('6', '9', 1))