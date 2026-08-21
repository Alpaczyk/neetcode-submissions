class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, i in enumerate(nums):
            if i in seen:
                return [seen[i], idx]
            
            seen[target - i] = idx 
        
        return -1
