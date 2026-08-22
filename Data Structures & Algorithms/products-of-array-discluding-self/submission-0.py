class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        pre = 1
        for i in range(len(nums)):
            ans[i] = pre
            pre *= nums[i]
        suf = 1
        for j in range(len(nums) - 1, -1, -1):
            ans[j] *= suf
            suf *= nums[j]
        
        return ans