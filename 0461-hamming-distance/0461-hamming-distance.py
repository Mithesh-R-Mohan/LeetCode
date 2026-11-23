class Solution(object):
    def hammingDistance(self, x, y):
        n = x ^ y
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c