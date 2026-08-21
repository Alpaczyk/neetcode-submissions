class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        contain = False
        for i in range(len(nums) + 1):
                for j in nums:
                        if i == j:
                                contain = True
                if not contain:
                        return i;
                else:
                        contain = False
        return 