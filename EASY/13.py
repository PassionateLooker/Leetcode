# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0

        s = s.replace('IV', 'IIII').replace('IX', "VIIII")
        s = s.replace('XL', 'XXXX').replace('XC', "LXXXX")
        s = s.replace('CD', 'CCCC').replace('CM', "DCCCC")

        for i in s:
            total += val_map[i]
        return total


