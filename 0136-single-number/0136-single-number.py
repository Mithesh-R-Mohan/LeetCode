class Solution(object):
    def singleNumber(self, nums):
        while nums:
            e=nums.pop()
            if e not in nums:
                return e
            else:
                nums.remove(e)