# 1184.
# Distance
# Between
# Bus
# Stops
#
# A
# bus
# has
# n
# stops
# numbered
# from
#
# 0
# to
# n - 1
# that
# form
# a
# circle.We
# know
# the
# distance
# between
# all
# pairs
# of
# neighboring
# stops
# where
# distance[i] is the
# distance
# between
# the
# stops
# number
# i and (i + 1) % n.
#
# The
# bus
# goes
# along
# both
# directions
# i.e.clockwise and counterclockwise.
#
# Return
# the
# shortest
# distance
# between
# the
# given
# start and destination
# stops.
#
# Example
# 1:
#
# Input: distance = [1, 2, 3, 4], start = 0, destination = 1
# Output: 1
# Explanation: Distance
# between
# 0 and 1 is 1 or 9, minimum is 1.
#
# Example
# 2:
#
# Input: distance = [1, 2, 3, 4], start = 0, destination = 2
# Output: 3
# Explanation: Distance
# between
# 0 and 2 is 3 or 7, minimum is 3.

class Solution:
    def distanceBetweenBusStops(self, distance, start, destination):
        addAll =0
        zeroToStart=0
        if start>destination:
            start,destination=destination,start
        for i in range(start,destination):
            addAll+=distance[i] #10
        for i in range(destination,len(distance)):
            zeroToStart+=distance[i]

        for i in range(0,start):

            zeroToStart += distance[i]

        return min(addAll,zeroToStart)
s=Solution()
print(s.distanceBetweenBusStops([1, 2, 3, 4],1,3))
