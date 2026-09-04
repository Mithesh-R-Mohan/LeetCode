class Solution(object):
    def majorityElement(self, nums):
        c=None
        count=0
        for n in nums:
            if count==0:
                c=n
            count+=1 if n==c else -1
        return c