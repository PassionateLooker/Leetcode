# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ("")
        if len(strs) == 1:
            return strs[0]

        pref = strs[0]
        plen = len(pref)

        for s in strs[1:]:
            while pref != s[0:plen]:
                pref = pref[0:(plen - 1)]
                plen -= 1

            if plen == 0:
                return ("")
        return (pref)



