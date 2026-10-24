class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlapping(a, b):
            # touching interval are also considered overlapping
            front = max(a[0], b[0])
            back = min(a[1], b[1])
            return back-front >= 0

        out = []
        intervals.sort()
        out.append(intervals[0])
        for i in range(1, len(intervals)):
            temp = out[-1]
            if isOverlapping(temp, intervals[i]):
                temp[0] = min(temp[0], intervals[i][0])
                temp[1] = max(temp[1], intervals[i][1])
                out[-1] = temp
            else:
                out.append(intervals[i])
        
        return out 