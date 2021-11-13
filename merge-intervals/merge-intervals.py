class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        ans = []
        
        for start, end in intervals:
            if not ans:
                ans.append([start, end])
            elif ans[-1][1] < start:
                ans.append([start, end])
            else:
                ans[-1][1] = max(ans[-1][1], end)
        
        return ans