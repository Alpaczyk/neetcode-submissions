class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        ans = []
        intervals = sorted(intervals, key=lambda x: x[0])
        prev = intervals[0]

        i = 1
        
        for i in range(len(intervals)):
            interval = intervals[i]

            if prev[1] >= interval[0]:
                prev[1] = max(prev[1], interval[1])
            else:
                ans.append(prev)
                prev = interval
        ans.append(prev)
        return ans
        