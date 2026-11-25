class Solution(object):
    def findComplement(self, num):
        bn=bin(num)[2:]
        inv=''.join('1' if x == '0' else '0' for x in bn)
        return int(inv,2)