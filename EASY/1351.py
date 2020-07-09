# 1351.
# Count
# Negative
# Numbers in a
# Sorted
# Matrix
# Easy
#
#
# Given
# a
# m * n
# matrix
# grid
# which is sorted in non - increasing
# order
# both
# row - wise and column - wise.
#
# Return
# the
# number
# of
# negative
# numbers in grid.
#
# Example
# 1:
#
# Input: grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
# Output: 8
# Explanation: There
# are
# 8
# negatives
# number in the
# matrix.


grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
def a(grid):
    cnt=0
    for i in grid:
        for j in i:
            if j<0:
                cnt+=1
    return cnt
print(a(grid))

