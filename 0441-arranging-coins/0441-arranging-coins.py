class Solution:
    def arrangeCoins(self, n):
        left, right = 1, n
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            coins_needed = mid * (mid + 1) // 2
            if coins_needed == n:
                return mid
            elif coins_needed < n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1        
        return ans