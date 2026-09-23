class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        l, s = [], nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if s == nums[i - 1]:
                    l.append(str(s))
                else:
                    l.append(str(s) + '->' + str(nums[i - 1]))
                s = nums[i]
        if s == nums[-1]:
            l.append(str(s))
        else:
            l.append(str(s) + '->' + str(nums[-1]))
        return l