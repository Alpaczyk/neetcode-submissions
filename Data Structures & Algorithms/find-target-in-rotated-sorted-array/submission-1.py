class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break
        
        def bs(nums, left, right, target):
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        if pivot == -1:
            left = 0
            right = len(nums) - 1
            return bs(nums, left, right, target)
        else:
            left1 = 0
            right1 = pivot
            left2 = pivot + 1
            right2 = len(nums) - 1
            return max(bs(nums, left1, right1, target), bs(nums, left2, right2, target))
        

