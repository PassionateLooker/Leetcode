#
# 1221. Split a String in Balanced Strings
#
# Balanced strings are those who have equal quantity of 'L' and 'R' characters.
#
# Given a balanced string s split it in the maximum amount of balanced strings.
#
# Return the maximum amount of splitted balanced strings.
#
#
#
# Example 1:
#
# Input: s = "RLRRLLRLRL"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

s = "RLLLLRRRLR"


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        cnt = 0
        for i in s:
            if i == 'R':
                balanced += 1
            else:
                balanced -= 1
            if not balanced:
                cnt += 1
        return cnt
