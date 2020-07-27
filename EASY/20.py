# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true


class Solution:
    def isValid(self, s):
        stac k =[]
        for i in range(len(s)):
            if self.isOpenParen(s[i]):
                stack.append(s[i])
            else:
                if len(stack )= =0:
                    return False
                o p =stack.pop()
                cur r =s[i]
                isVali d =self.isParenSameType(op ,curr)
                if not isValid:
                    return False
        return len(stack )= =0





    def isOpenParen(self ,p):
        if p== '[' or p == '(' or p == '{':
            return True
        return False

    def isParenSameType(self, p, op):
        if p == '[' and op == ']':
            return True
        elif p == '{' and op == '}':
            return True
        elif p == '(' and op == ')':
            return True
        else:
            return False


